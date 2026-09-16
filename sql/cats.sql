-- Задача 2
-- Как выбрать всех сотрудников, у которых нет кошек?

CREATE TABLE pets (
    employee_id INTEGER NOT NULL,
    animal TEXT NOT NULL
);

INSERT INTO pets (employee_id, animal) VALUES
    (1, 'кошка'),
    (2, 'кошка'),
    (2, 'собака'),
    (3, 'пони'),
    (4, 'питон'),
    (4, 'мышь'),
    (4, 'хомяк');

-- Напишите SELECT ниже.

