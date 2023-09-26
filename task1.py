import math

x = float(input("X: "))
y = float(input("Y: "))
z = float(input("Z: "))

a = (math.tan(math.sqrt(x - 1)) - ((abs(y)) ** 1 / 4)) / x ** 1 / 5 + y ** 1 / 6 + math.log(4)
b = x ** 1 / 3 + math.sin(z) + math.cosh(x) - math.log1p(y)

print("a= {:.4f}, b= {:.4f}".format(a, b))










