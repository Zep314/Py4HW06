"""
Шахматный модуль - содержит функции для решения и проверки решения задачи о 8 ферзях
"""


def __q8_test_flat(flat_desk: list) -> bool:
    """
    Проверяем расстановку по вертикалям и диагоналям в "плоской" записи задачи
    :param flat_desk:
    :return:
    """
    for i in range(8):
        for j in range(8):
            if (i != j) and ((flat_desk[i] == flat_desk[j]) or (abs(flat_desk[i] - flat_desk[j]) == (i - j))):
                return False
    return True


def q8_test(desk_set: list) -> bool:
    """
    Проверяем расстановку ферзей в общей записи задачи
    :param desk_set:
    :return:
    """
    if len(tuple([x[1] for x in desk_set])) != 8:  # Проверяем горизонтали
        return False
    else:
        return __q8_test_flat([x[0] - 1 for x in desk_set])  # Проверяем вертикали и диагонали в "плоской" записи


def print_chess_desk(desk_set: list):
    """
    Красиво выводим на печать шахматную доску с установленными фигурами
    :param desk_set:
    :return:
    """
    h_line = "+---" * 8 + "+"
    for i in range(8):
        print(h_line)
        for j in range(8):
            print(f'| {"*" if ((j + 1) == desk_set[i][0]) and ((i + 1) == desk_set[i][1]) else " "} ', end='')
        print("|")
    print(h_line)


def my_arrangement() -> list:
    """
    Возвращаем ВСЕ решения задачи о расстановке 8-ми ферзей на шахматном моле
    :return:
    """

    def __checking() -> bool:  # Проверка на границу, вертикаль и диагональ урезанная!
        nonlocal index, chessboard  # переменные из функции на уровень выше
        if index == 0:
            return True
        if chessboard[index] > 7:  # вышли за границу доски
            chessboard[index] = 0
            index -= 1
            return False
        for i in range(index):

            if (chessboard[index] == chessboard[i]) or \
                    ((abs(chessboard[index] - chessboard[i])) == (index - i)):  # Проверка вертикали и диагонали
                return False
        return True

    chessboard = [0, 0, 0, 0, 0, 0, 0, 0]  # "Плоская" запись ферзей на доске
    ret = []  # Тут собираем все правильные решения
    while chessboard[0] < 8:
        index = 0
        while index < 8:
            if __checking():
                index += 1
            else:
                chessboard[index] += 1
            if chessboard[0] > 7:  # Правильных решений больше не осталось
                break
        if chessboard[0] < 8:
            ret.append(tuple([(chessboard[i] + 1, i + 1) for i in range(8)]))  # Сохраняем правильное решение
            chessboard[-1] += 1
    return ret
