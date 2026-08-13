# Interview

Тестовое задание. Окружение — Docker + `make`. Каталог проекта смонтирован в контейнер (`.:/app`).

## Карта задач

| Задача | Условие | Проверка |
|--------|---------|----------|
| 1 | [`task1-ai-agents.md`](task1-ai-agents.md) | устно |
| 2 | [`task2-cats.md`](task2-cats.md), правки в [`sql/cats.sql`](sql/cats.sql) | `make sql-cats` |
| 3 | [`task3-messages.md`](task3-messages.md), правки в [`sql/messages.sql`](sql/messages.sql) | `make sql-messages` |
| 4 | [`task4-ai-client.md`](task4-ai-client.md), правки в [`src/ai_client.py`](src/ai_client.py) | `make test-ai-client` |
| 5 | [`task5-resume-flow.md`](task5-resume-flow.md) | устно |

Список всех `make`-команд:

```
make
```

## Запуск окружения

```
make up
```
