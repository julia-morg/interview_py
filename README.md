# Interview

Тестовое задание. Окружение — Docker + `make`. Каталог проекта смонтирован в контейнер (`.:/app`), локальные правки сразу видны.

## Карта задач

| Задача | Условие | Проверка |
|--------|---------|----------|
| 1–2 | [`task1-2-chess.md`](task1-2-chess.md), код в `chess.py` / `src/` | `make test-rotation`, `make test-pawn` |
| 3 | [`task3-cats.md`](task3-cats.md), правки в [`sql/cats.sql`](sql/cats.sql) | `make sql-cats` |
| 4 | [`task4-phones.md`](task4-phones.md), правки в [`sql/phones.sql`](sql/phones.sql) | `make sql-phones` |
| 5 | [`task5-messages.md`](task5-messages.md), правки в [`sql/messages.sql`](sql/messages.sql) | `make sql-messages` |
| 6 | [`task6-arch.md`](task6-arch.md) | письменно / устно |
| 7 | [`task7-ai-client.md`](task7-ai-client.md), правки в [`src/ai_client.py`](src/ai_client.py) | `make test-ai-client` |
| 8 | [`task8-resume-flow.md`](task8-resume-flow.md) | устно |

Список всех `make`-команд:

```
make
```

## Запуск окружения

```
make up
make shell
make down
```

Шахматы с произвольными ходами:

```
make chess MOVES="e2-e4 e7-e5"
```

Все автотесты задач 1–2:

```
make test
```
