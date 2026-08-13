import asyncio

import httpx
import pytest

from src.ai_client import AIClient, AIProviderError


def run(coro):
    return asyncio.run(coro)


def client(handler, *, sleep=None, timeout=0.25, max_attempts=3):
    kwargs = {
        "base_url": "https://ai.example.test",
        "api_key": "test-key",
        "timeout": timeout,
        "max_attempts": max_attempts,
        "transport": httpx.MockTransport(handler),
    }
    if sleep is not None:
        kwargs["sleep"] = sleep
    return AIClient(**kwargs)


def test_retries_5xx_and_keeps_idempotency_key():
    requests = []

    def handler(request):
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(503, json={"error": "temporary"})
        return httpx.Response(200, json={"result": "ok"})

    result = run(client(handler, sleep=lambda _: _done()).analyze("position", "req-42"))

    assert result == "ok"
    assert len(requests) == 2
    assert {r.headers.get("Idempotency-Key") for r in requests} == {"req-42"}


def test_uses_configured_timeout():
    seen_timeout = None

    def handler(request):
        nonlocal seen_timeout
        seen_timeout = request.extensions.get("timeout")
        return httpx.Response(200, json={"result": "ok"})

    run(client(handler, timeout=0.25).analyze("position", "req-timeout"))

    assert seen_timeout == {"connect": 0.25, "read": 0.25, "write": 0.25, "pool": 0.25}


def test_429_honors_retry_after():
    calls = 0
    delays = []

    async def fake_sleep(delay):
        delays.append(delay)

    def handler(request):
        nonlocal calls
        calls += 1
        if calls == 1:
            return httpx.Response(429, headers={"Retry-After": "2"})
        return httpx.Response(200, json={"result": "ok"})

    assert run(client(handler, sleep=fake_sleep).analyze("position", "req-429")) == "ok"
    assert calls == 2
    assert delays == [2.0]


def test_does_not_retry_non_retryable_4xx():
    calls = 0

    def handler(request):
        nonlocal calls
        calls += 1
        return httpx.Response(403, json={"error": "forbidden"})

    with pytest.raises(AIProviderError):
        run(client(handler).analyze("position", "req-403"))
    assert calls == 1


def test_retries_network_error_and_stops_at_limit():
    calls = 0

    def handler(request):
        nonlocal calls
        calls += 1
        raise httpx.ConnectError("network down", request=request)

    with pytest.raises(AIProviderError):
        run(client(handler, sleep=lambda _: _done(), max_attempts=3).analyze("position", "req-net"))
    assert calls == 3


@pytest.mark.parametrize("payload", [{}, {"result": ""}, {"result": None}, ["not", "object"]])
def test_rejects_invalid_success_payload(payload):
    def handler(request):
        return httpx.Response(200, json=payload)

    with pytest.raises(AIProviderError):
        run(client(handler).analyze("position", "req-json"))


async def _done():
    return None
