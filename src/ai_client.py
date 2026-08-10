import asyncio
from collections.abc import Awaitable, Callable

import httpx


class AIProviderError(RuntimeError):
    pass


class AIClient:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        timeout: float = 3.0,
        max_attempts: int = 3,
        transport: httpx.AsyncBaseTransport | None = None,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.max_attempts = max_attempts
        self.transport = transport
        self.sleep = sleep

    async def analyze(self, prompt: str, request_id: str) -> str:
        async with httpx.AsyncClient(
            base_url=self.base_url,
            transport=self.transport,
        ) as client:
            response = await client.post(
                "/analyze",
                json={"prompt": prompt},
                headers={"Authorization": f"Bearer {self.api_key}"},
            )
            response.raise_for_status()
            return response.json()["result"]
