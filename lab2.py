from math import *
import matplotlib.pyplot as plt
import numpy as np


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
    a = float(input("a = "))
    b = float(input("b = "))

    x_vector = np.linspace(a, b, 500)

    def f(x):
        if x >= 0:
            y = exp(x) + x
        else:
            y = sin(x) + 1
        return y

    y_vector = []
    for x in x_vector:
        y_vector.append(f(x))

    plt.plot(x_vector, y_vector)
    plt.show()


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


def task6():
    def is_happy(number):
        ticket_str = str(number).zfill(6)  # Преобразуем номер билета в строку и дополним нулями слева до 6 символов
        first_half = [int(char) for char in ticket_str[:3]]  # Получаем первую половину номера билета
        second_half = [int(char) for char in ticket_str[3:]]  # Получаем вторую половину номера билета

        if sum(first_half) == sum(second_half):
            return True
        else:
            return False

    ticket_number = int(input("Введите номер билета: "))
    print(is_happy(ticket_number))


def task8():
    def calculate_product(n):
        product = 1
        for i in range(1, n + 1):
            numerator = cos(i)
            denominator = sin(2 * i)
            product *= numerator / denominator
        return product

    n = int(input("Введите значение n: "))
    result = calculate_product(n)
    print("Результат - {:.4f}".format(result))


def task9():
    def ex_first():
        result = 0

        for i in range(1, 9):
            for j in range(1, i + 1):
                term = (pow(j, cos(i)) + pow(i, cos(j))) ** 2
                result += term

        return result

    def ex_second():
        result = 1

        for i in range(1, 6):
            product = 1
            for j in range(1, i + 1):
                term = sin(j**cos(i))
                product *= term
            result *= product

        return result

    def ex_third():
        result = 1
        for i in range(1, 9):
            product = 1
            for j in range(i, (2*i-1)+1):
                sum1 = 0
                for k in range(i+j, 2*(i+j)+1):
                    sum2 = 0
                    term = 2*cos(j)-3*log(i+0.5*k)
                    product *= term
                result = product

        return result

    print("Значение первого выражения = {:.4f}".format(ex_first()))
    print("Значение второго выражения = {:.4f}".format(ex_second()))
    print("Значение третьего выражения = {:.4f}".format(ex_third()))

    """def ex_first():
        result_sum = 0

        for i in range(1, 9):
            inner_sum = 0

            for j in range(1, i + 1):
                inner_result = (j ** cos(i) + i ** cos(j)) ** 2
                inner_sum += inner_result

            result_sum += inner_sum
            print(result_sum)
            

    print("Значение первого выражения = {:.4f}".format(ex_first()))"""


task9()
