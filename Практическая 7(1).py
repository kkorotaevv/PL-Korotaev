print('ВАРИАНТ 9')
print('ЗАДАНИЕ 1')


def f(n):
    a = 0
    while n > 0:
        a += n % 10
        n = n // 10
    return a


b = int(input("Введите число: "))
c = 0
while b > 0:
    b -= f(b)
    c += 1

print("Через " + str(c) + " действий")


print('ЗАДАНИЕ 2')
from random import randint
x = [randint(1, 10) for i in range(5)]
y = [randint(1, 10) for i in range(5)]
z = [randint(1, 10) for i in range(5)]
print('Первый массив', x)
print('Второй массив', y)
print('Третий массив', z)
arf = 0
prz = 1
summa = 0
for i in x:
    prz *= i
    summa += i
print('Произведение элементов в 1 массиве', prz)
arf = summa / 5
print('Среднеарифметическое значение в 1 массиве', arf)
arf = 0
prz = 1
summa = 0
for i in y:
    prz *= i
    summa += i
print('Произведение элементов в 2 массиве', prz)
arf = summa / 5
print('Среднеарифметическое значение в 2 массиве', arf)
arf = 0
prz = 1
summa = 0
for i in z:
    prz *= i
    summa += i
print('Произведение элементов в 3 массиве', prz)
arf = summa / 5
print('Среднеарифметическое значение в 3 массиве', arf)