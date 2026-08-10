import os
import subprocess
import sys

import pytest

moves_key = pytest.StashKey[str]()

TESTS_DIR = os.path.join(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(TESTS_DIR)
CHESS = os.path.join(ROOT_DIR, "chess.py")


@pytest.fixture
def run_chess_case(request):
    def run_file(path):
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()

        moves = lines[0].strip()
        moves_desc = moves or "(no moves)"
        request.node.stash[moves_key] = moves_desc
        is_correct = lines[1].strip() != "error"

        cmd = [sys.executable, CHESS] + (moves.split() if moves else [])
        result = subprocess.run(cmd, capture_output=True, text=True)

        if is_correct:
            assert result.returncode == 0, (
                f"Moves are correct, but chess.py thinks there is an error: {moves_desc}"
            )
        else:
            assert result.returncode != 0, (
                f"Moves are invalid, but chess.py does not detect that: {moves_desc}"
            )

    return run_file


def pytest_configure(config):
    config.option.reportchars = ""


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        report._chess_moves = item.stash.get(moves_key, "")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    passed = terminalreporter.stats.get("passed", [])
    failed = terminalreporter.stats.get("failed", [])
    if not passed and not failed:
        return

    terminalreporter.write_sep("=", "test summary")
    for report in passed:
        moves = getattr(report, "_chess_moves", "") or ""
        suffix = f" - {moves}" if moves else ""
        terminalreporter.write_line(f"PASSED {report.nodeid}{suffix}", green=True)
    for report in failed:
        message = ""
        if report.longrepr is not None:
            text = str(report.longrepr)
            if "AssertionError: " in text:
                message = "AssertionError: " + text.split("AssertionError: ", 1)[1].split("\n", 1)[0]
            else:
                message = text.split("\n", 1)[0]
        if message:
            terminalreporter.write_line(f"FAILED {report.nodeid} - {message}", red=True)
        else:
            moves = getattr(report, "_chess_moves", "") or ""
            suffix = f" - {moves}" if moves else ""
            terminalreporter.write_line(f"FAILED {report.nodeid}{suffix}", red=True)
