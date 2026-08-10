#!/usr/bin/env python3
import sqlite3
import sys
from pathlib import Path


def statements_from_sql(sql: str) -> list[str]:
    result = []
    for chunk in sql.split(";"):
        lines = []
        for line in chunk.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("--"):
                continue
            lines.append(line)
        statement = "\n".join(lines).strip()
        if statement:
            result.append(statement)
    return result


def is_select(statement: str) -> bool:
    head = statement.lstrip().split(None, 1)[0].upper()
    return head in {"SELECT", "WITH"}


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path-to.sql>", file=sys.stderr)
        return 1

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Файл не найден: {path}", file=sys.stderr)
        return 1

    statements = statements_from_sql(path.read_text(encoding="utf-8"))
    if not statements:
        print(f"Файл {path} пуст", file=sys.stderr)
        return 1

    selects = [s for s in statements if is_select(s)]
    if not selects:
        print(f"В файле {path} нет SELECT — напишите запрос", file=sys.stderr)
        return 1

    conn = sqlite3.connect(":memory:")
    try:
        cur = conn.cursor()
        last_select_rows = None
        last_columns = None

        for statement in statements:
            cur.execute(statement)
            if is_select(statement):
                last_columns = [d[0] for d in cur.description] if cur.description else []
                last_select_rows = cur.fetchall()

        if last_columns:
            print(" | ".join(last_columns))
            print("-+-".join("-" * len(c) for c in last_columns))
        for row in last_select_rows or []:
            print(" | ".join("" if value is None else str(value) for value in row))
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
