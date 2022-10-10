print('ВАРИАНТ 6')
print('ЗАДАНИЕ 1')
from random import *

a = 0
b = 1
l = [randint(1, 10) for i in range(10)]
print('Список l =', l)
for i in l:
    a += i
b *= i
print('Сумма всех чисел списка =', a)
print('Произведение всех чисел списка =', b)

print('ЗАДАНИЕ 2')
d = [randint(0, 5) for i in range(20)]
z = 0
x = 20
c = 0
print('Исходный cписок d =', d)
for i in d:
    z += i
c = z / 20
for i in range(x):
    if d[i] != 0:
        d[i] = c
print('Изменённый список d =', d)
