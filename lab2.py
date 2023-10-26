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
    print("Число является простым -", is_prime(number),", Число является положительным -", is_positive(number))


def task2():
    pass

task1()

