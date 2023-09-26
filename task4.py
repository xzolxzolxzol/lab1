import math

r = float(input("Радиус меньшего основания (r)="))
R = float(input("Радиус большего основания (R)="))
h = float(input("Высота конуса (h)="))

cone_generatrix = math.sqrt(h ** 2 + (R - r) ** 2)

print ("Образующая (l)= {:.4f}". format(cone_generatrix))

