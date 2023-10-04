"""
Модуль проверки корректности введенной даты
"""


def __is_leap_year(year):
    """
    Проверка високосный год, или нет
    :param year:
    :return: True, если год високосный
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return True if year % 4 == 0 else False


def is_valid_date(day: int, month: int, year: int) -> bool:
    """
    Проверка на корректность григорианскому календарю введенную дату
    :param day: день
    :param month: месяц
    :param year: год
    :return: Верно/неверно
    """
    if (year < 0) or (year > 10000):
        return False
    elif (month < 0) or (month > 13):
        return False
    elif day < 0:
        return False
    elif month in [1, 3, 5, 7, 8, 10, 12] and (day > 32):
        return False
    elif month in [4, 6, 9, 11] and (day > 31):
        return False
    elif month == 2:
        if __is_leap_year(year) and (day > 29):
            return False
        elif (not __is_leap_year(year)) and (day > 28):
            return False
        else:
            return True
    else:
        return True


def is_valid_date_tuple(date_tuple:  tuple) -> bool:
    """
    Функция проверки даты, которая принимает на проверку кортеж из 3-х чисел
    :param date_tuple:
    :return:
    """
    if len(date_tuple) != 3:
        return False
    return is_valid_date(date_tuple[0], date_tuple[1], date_tuple[2])
