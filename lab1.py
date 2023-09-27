import math


def task1():
    x = float(input("X: "))
    y = float(input("Y: "))
    z = float(input("Z: "))

    a = (math.tan(math.sqrt(x - 1)) - ((abs(y)) ** 1 / 4)) / x ** 1 / 5 + y ** 1 / 6 + math.log(4)
    b = x ** 1 / 3 + math.sin(z) + math.cosh(x) - math.log1p(y)

    print("a= {:.4f}, b= {:.4f}".format(a, b))


def task2():
    x = float(input("X= "))

    a = 1
    b = 4

    f = math.sqrt(x + a) + (((x ** 2) + b) / x)

    print("f(x)= {:.4f}".format(f))


def task3():
    x = float(input("X= "))

    f = math.log(x ** 2 + 1, 3) - 3.25 * x

    print("F(x)= {:.4f}".format(f))


def task4():
    r = float(input("Радиус меньшего основания (r)="))
    R = float(input("Радиус большего основания (R)="))
    h = float(input("Высота конуса (h)="))

    cone_generatrix = math.sqrt(h ** 2 + (R - r) ** 2)

    print("Образующая (l)= {:.4f}".format(cone_generatrix))


def task5():
    V = float(input("Скорость парома в стоячей воде (V)= "))
    v = float(input("Скорость течения реки (v)= "))
    h = float(input("Ширина реки (h)= "))

    angle = math.atan(v / V)

    if V > v:
        print(math.degrees(angle))
    else:
        print("Скорость парома должна быть больше скорости течения реки!")


def task6():
    S = float(input("Площадь поверхности шара (S)= "))
    if S > 0:
        pass
    else:
        print("Ошибка: площадь меньше или равна нулю")
    distance = float(input("Расстояние от центра шара до сечения (l)= "))
    if distance > 0:
        pass
    else:
        print("Ошибка: расстояние меньше или равно нулю")

    R = math.sqrt(S / 4 * math.pi)  # Радиус шара
    r = math.sqrt(abs(R**2-distance**2))  # Радиус сечения
    if r>0:
        pass
    else:
        print("Ошибка: квадратный корень меньше нуля")
    cross_sec_area =  math.pi * r**2

    print ("Площадь поперечного сечения = {:.4f}". format(cross_sec_area))


    def task7():
        pass



task6()
