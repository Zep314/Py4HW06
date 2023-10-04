"""
Функция проверки введенной даты из командной строки
"""

# Задание 1
# В модуль с проверкой даты добавьте возможность запуска в терминале с
# передачей даты на проверку.

import sys
import my_utils as mu

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) != 4:
        print("""        Ошибка в параметрах! 
        Запускайте команду в следующем виде:
        ch_date <DD> <MM> <YYYY>""")
    try:
        print(sys.argv)
        x = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        print(f'{x = } {"Дата корректна!" if mu.date_module.is_valid_date_tuple(x) else "Ошибка в дате!"}')
    except ValueError:
        print("Ошибка ввода!")
    except IndexError:
        print("Ошибка в количестве параметров!")


# Результат работы:
# C:\Work\python\dz4\Py4HW06>python ch_date.py 1 2 2023
# x = (1, 2, 2023) Дата корректна!
#
# C:\Work\python\dz4\Py4HW06>python ch_date.py 41 2 2023
# x = (41, 2, 2023) Ошибка в дате!
#
# C:\Work\python\dz4\Py4HW06>python ch_date.py 41 2
#         Ошибка в параметрах!
#         Запускайте команду в следующем виде:
#         ch_date <DD> <MM> <YYYY>
# Ошибка ввода!
#
# C:\Work\python\dz4\Py4HW06>python ch_date.py 29 02 1900
# x = (29, 2, 1900) Ошибка в дате!
#
# C:\Work\python\dz4\Py4HW06>python ch_date.py 29 02 1904
# x = (29, 2, 1904) Дата корректна!
#
# C:\Work\python\dz4\Py4HW06>python ch_date.py 29 02 qqq
# Ошибка ввода!
#
# C:\Work\python\dz4\Py4HW06>
