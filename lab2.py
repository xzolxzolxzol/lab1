from math import *


def task1():
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_positive(num):
        if num > 0:
            return True
        else:
            return False

    number = float(input("Введите число - "))
    print("Число является простым -", is_prime(number), ", Число является положительным -", is_positive(number))


def task2():
    a = float(input())
    b = float(input())

    x_list = list(range(a, b))

    if x_list >= 0:
        f = exp(x_list) + x_list
    else:
        f = sin(x_list) + 1
    print("f(x)= {:.4f}".format(f))

    pass


def task3():
    def number_in_new_numeral_system(number, base):
        if number == 0:
            return '0'

        digits = []
        while number > 0:
            # Остаток от деления - это цифра в новой системе счисления
            remainder = number % base
            # Добавляем цифру в начало списка
            digits.insert(0, str(remainder))
            number = number // base

        return ''.join(digits)

    number = int(input("Введите число в десятичной системе счисления: "))
    base = int(input("Введите основание новой системы счисления: "))

    result = number_in_new_numeral_system(number, base)
    print(f"Результат: {result}")


def task5():
    def find_smallest_largest_absolute_value(a, b, c):
        absolute_values = [a, b, c]


        smallest = min(absolute_values)
        largest = max(absolute_values)

        return smallest, largest

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))

    smallest_value, largest_value = find_smallest_largest_absolute_value(a, b, c)

    print(f"Наименьшее абсолютное значение: {smallest_value}")
    print(f"Наибольшее абсолютное значение: {largest_value}")


task5()
