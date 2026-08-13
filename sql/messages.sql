-- Задача 3
-- Таблица сообщений:
--
-- | id | external_id | chat_id | direction |
-- |----|-------------|---------|-----------|
-- |  1 | ext-100     |       1 | in        |
-- |  2 | ext-100     |       1 | in        |
-- |  3 | ext-200     |       1 | out       |
-- |  4 | ext-100     |       2 | in        |
-- |  5 | ext-100     |       2 | out       |
-- |  6 | ext-300     |       3 | in        |
-- |  7 | ext-300     |       3 | out       |
-- |  8 | ext-400     |       4 | out       |
-- |  9 | ext-400     |       4 | out       |
-- | 10 | ext-400     |       4 | in        |
-- | 11 | ext-500     |       5 | in        |
--
-- direction: in — входящее, out — исходящее.
-- external_id — id сообщения во внешней системе.
--
-- 1. Найдите чаты, в которых есть дубли сообщений.
-- 2. Удалите дубликаты.
-- 3. Измените схему и запрос вставки так, чтобы повторная или одновременная
--    доставка одного сообщения не создавала дубли и не завершалась ошибкой.
--    Покажите решение на повторной доставке ext-500 в чат 5.
--
-- Ниже: создание таблицы, тестовые данные, затем ваши SQL-команды.

CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    external_id TEXT NOT NULL,
    chat_id INTEGER NOT NULL,
    direction TEXT NOT NULL
);

INSERT INTO messages (id, external_id, chat_id, direction) VALUES
    (1,  'ext-100', 1, 'in'),
    (2,  'ext-100', 1, 'in'),
    (3,  'ext-200', 1, 'out'),
    (4,  'ext-100', 2, 'in'),
    (5,  'ext-100', 2, 'out'),
    (6,  'ext-300', 3, 'in'),
    (7,  'ext-300', 3, 'out'),
    (8,  'ext-400', 4, 'out'),
    (9,  'ext-400', 4, 'out'),
    (10, 'ext-400', 4, 'in'),
    (11, 'ext-500', 5, 'in');

-- Напишите SQL ниже.
