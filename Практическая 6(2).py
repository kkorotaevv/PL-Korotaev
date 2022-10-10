print('ВАРИАНТ 3')
print('ЗАДАНИЕ 1')
from random import randint

summa = 0
n = int(input('Введите длину массива '))
D = [randint(1, 100) for i in range(n)]
print('Список D =', D)
for i in D:
    if D.index(i) % 2 == 0:
        summa += i
print('Сумма элементов с нечётными индексами = ', summa)

print('ЗАДАНИЕ 2')

l = [randint(1, 30) for i in range(8)]
print('Исходный список -', l)
a = 8
for i in range(a):
    if l[i] < 15:
        l[i] = l[i] * 2
print('Изменённый список -', l)
