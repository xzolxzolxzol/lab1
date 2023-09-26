import math

def find_angle(V, v):
    angle = math.atan(v / V)
    return math.degrees(angle)

V = float(input("Скорость парома в стоячей воде (V)= "))
v = float (input("Скорость течения реки (v)= "))
h = float (input("Ширина реки (h)= "))

# Проверяем, может ли паром преодолеть реку
if V > v:
    angle = find_angle(V, v)
    print(round(angle, 4))
else:
    print("Паром не может преодолеть реку с такими параметрами.")