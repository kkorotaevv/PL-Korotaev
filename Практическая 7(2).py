print('ВАРИАНТ 3')
print('ЗАДАНИЕ 1')
import math


def c1(k1, k2):
    gip = k1 ** 2 + k2 ** 2
    c = math.sqrt(gip)
    return c


def c2(k1, k2):
    gip = k1 ** 2 + k2 ** 2
    c = math.sqrt(gip)
    return c

k1 = int(input('Введите 1 катет '))
k2 = int(input('Введите 2 катет '))
k3 = int(input('Введите 3 катет '))
k4 = int(input('Введите 4 катет '))


if c1(k1, k2) > c2(k3, k4):
    print("Первый больше")
else:
    print("Второй больше")

print('ЗАДАНИЕ 2')
a = input('Напишите строку - ').lower().split(' ')
for i in range(len(a)):
    a[i] = ''.join(sorted(a[i]))
print(''.join(a))