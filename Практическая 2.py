import math

x = int(input('Введите переменную x: '))
t = int(input('Введите переменную t: '))
Z = ((9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - math.fabs(math.sin(t)))) * math.e ** x
print('Z = {0:.2f}'.format(Z))