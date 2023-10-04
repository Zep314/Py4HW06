
# Задание 2
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар
# чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#
# Задание 3
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты
# и выведите 4 успешных расстановки.

from random import randint

import my_utils as mu

if __name__ == '__main__':
    print("---=== Тестирование модуля работы с датой ===---")
    date_tests = ((1, 1, 2001),  # Заполняем день, месяц и год
                  (29, 2, 2020),
                  (29, 2, 1900),
                  (28, 2, 1900),
                  (-1, 11, 2021),
                  )
    for x in date_tests:
        print(f'{x = } {"Корректно" if mu.date_module.is_valid_date_tuple(x) else "Ошибка в дате!"}')

    print("\n---=== Шахматный модуль ===---")

    chess_q8_test_list = [
        (7, 1),
        (1, 2),
        (3, 3),
        (8, 4),
        (6, 5),
        (4, 6),
        (2, 7),
        (5, 8),
    ]

    print(f'Расстановка 8 ферзей на доске{" не" if not mu.chess.q8_test(chess_q8_test_list) else ""} корректна!')
    print("Отображение поля:")
    mu.chess.print_chess_desk(chess_q8_test_list)

    print("\nСлучайно расставленные фигуры. Проверка на расстановку:")
    for _ in range(4):
        desk = [(randint(1, 8), i) for i in range(1, 8)]
        print(f'Координаты фигур: {desk}, расстановка{" не" if not mu.chess.q8_test(desk) else ""} корректна')
        # print(desk, mu.chess.q8_test(desk))
        # if mu.chess.q8_test(desk):
        #     mu.chess.print_chess_desk(desk)

    print("\n4 удачные комбинации расстановки:")
    arrangement = mu.chess.my_arrangement()
    for x in range(4):
        r = randint(0, len(arrangement))
        mu.chess.print_chess_desk(arrangement[r])
        print(f'Координаты фигур: {arrangement[r]}, расстановка{" не" if not mu.chess.q8_test(arrangement[r]) else ""} корректна')
        print()

# Результат работы:
# C:\Work\python\dz4\Py4HW06\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW06/main.py
# ---=== Тестирование модуля работы с датой ===---
# x = (1, 1, 2001) Корректно
# x = (29, 2, 2020) Корректно
# x = (29, 2, 1900) Ошибка в дате!
# x = (28, 2, 1900) Корректно
# x = (-1, 11, 2021) Ошибка в дате!
#
# ---=== Шахматный модуль ===---
# Расстановка 8 ферзей на доске корректна!
# Отображение поля:
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   | * |   |
# +---+---+---+---+---+---+---+---+
# | * |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   | * |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   |   | * |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   | * |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   | * |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   | * |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   | * |   |   |   |
# +---+---+---+---+---+---+---+---+
#
# Случайно расставленные фигуры. Проверка на расстановку:
# Координаты фигур: [(3, 1), (2, 2), (4, 3), (1, 4), (8, 5), (2, 6), (5, 7)], расстановка не корректна
# Координаты фигур: [(5, 1), (6, 2), (3, 3), (3, 4), (1, 5), (2, 6), (2, 7)], расстановка не корректна
# Координаты фигур: [(2, 1), (6, 2), (5, 3), (2, 4), (3, 5), (3, 6), (5, 7)], расстановка не корректна
# Координаты фигур: [(3, 1), (5, 2), (7, 3), (5, 4), (6, 5), (2, 6), (4, 7)], расстановка не корректна
#
# 4 удачные комбинации расстановки:
# +---+---+---+---+---+---+---+---+
# |   | * |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   | * |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   |   | * |
# +---+---+---+---+---+---+---+---+
# |   |   | * |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# | * |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   | * |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   | * |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   | * |   |   |   |
# +---+---+---+---+---+---+---+---+
# Координаты фигур: ((2, 1), (6, 2), (8, 3), (3, 4), (1, 5), (4, 6), (7, 7), (5, 8)), расстановка корректна
#
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   | * |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   | * |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# | * |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   | * |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   | * |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   |   | * |
# +---+---+---+---+---+---+---+---+
# |   | * |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   | * |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# Координаты фигур: ((6, 1), (3, 2), (1, 3), (7, 4), (5, 5), (8, 6), (2, 7), (4, 8)), расстановка корректна
#
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   | * |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   | * |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# | * |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   |   | * |
# +---+---+---+---+---+---+---+---+
# |   |   |   | * |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   | * |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   | * |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   | * |   |   |   |
# +---+---+---+---+---+---+---+---+
# Координаты фигур: ((6, 1), (3, 2), (1, 3), (8, 4), (4, 5), (2, 6), (7, 7), (5, 8)), расстановка корректна
#
# +---+---+---+---+---+---+---+---+
# |   |   | * |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   | * |   |   |
# +---+---+---+---+---+---+---+---+
# |   | * |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   | * |   |
# +---+---+---+---+---+---+---+---+
# | * |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   | * |   |   |   |   |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   |   |   |   | * |
# +---+---+---+---+---+---+---+---+
# |   |   |   |   | * |   |   |   |
# +---+---+---+---+---+---+---+---+
# Координаты фигур: ((3, 1), (6, 2), (2, 3), (7, 4), (1, 5), (4, 6), (8, 7), (5, 8)), расстановка корректна
#
#
# Process finished with exit code 0
