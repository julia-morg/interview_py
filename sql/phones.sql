-- Задача 4
-- Имеется база со следующими таблицами:
--
-- CREATE TABLE `users` (
--   `id` INT(11) NOT NULL AUTO_INCREMENT,
--   `name` VARCHAR(255) DEFAULT NULL,
--   `gender` INT(11) NOT NULL COMMENT '0 - не указан, 1 - мужчина, 2 - женщина.',
--   `birth_date` INT(11) NOT NULL COMMENT 'Дата в unixtime.',
--   PRIMARY KEY (`id`)
-- );
-- CREATE TABLE `phone_numbers` (
--   `id` INT(11) NOT NULL AUTO_INCREMENT,
--   `user_id` INT(11) NOT NULL,
--   `phone` VARCHAR(255) DEFAULT NULL,
--   PRIMARY KEY (`id`)
-- );
--
-- Напишите запрос, возвращающий имя и число указанных телефонных номеров
-- девушек в возрасте от 18 до 22 лет.
-- Оптимизируйте таблицы и запрос при необходимости.
--
-- Ниже SQLite-совместимая схема, место для индексов, тестовые данные и ваш SELECT.

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    gender INTEGER NOT NULL,
    birth_date INTEGER NOT NULL
);

CREATE TABLE phone_numbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    phone TEXT
);


INSERT INTO users (id, name, gender, birth_date) VALUES
    (1, 'Анна', 2, strftime('%s', 'now', '-20 years')),
    (2, 'Мария', 2, strftime('%s', 'now', '-19 years')),
    (3, 'Ольга', 2, strftime('%s', 'now', '-25 years')),
    (4, 'Катя', 2, strftime('%s', 'now', '-17 years')),
    (5, 'Иван', 1, strftime('%s', 'now', '-20 years')),
    (6, 'Лена', 2, strftime('%s', 'now', '-21 years')),
    (7, 'Даша', 2, strftime('%s', 'now', '-18 years')),
    (8, 'Саша', 0, strftime('%s', 'now', '-19 years'));

INSERT INTO phone_numbers (user_id, phone) VALUES
    (1, '+79001111111'),
    (1, '+79001111112'),
    (2, '+79002222222'),
    (3, '+79003333333'),
    (3, '+79003333334'),
    (3, '+79003333335'),
    (4, '+79004444444'),
    (5, '+79005555555'),
    (5, '+79005555556');

-- Напишите SELECT ниже.
