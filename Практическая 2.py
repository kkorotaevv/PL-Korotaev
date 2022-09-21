import math

x = float(input('Введите x '))
y = float(input('Введите y '))
z = float(input('Введите z '))

s = math.fabs(x ** (y / x) - math.pow((y / x), 1 / 3)) + (y - x) * ((math.cos(y) - (z / (y - x))) / (1 + (y - x) ** 2))

print('Ответ: s = {0:.5f}'.format(s))
