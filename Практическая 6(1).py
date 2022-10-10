print('ВАРИАНТ 8')
print('ЗАДАНИЕ 1')
from random import randint
l = [randint(1, 100) for i in range(10)]
print('Максимальное число из списка - ', max(l))
l.remove(max(l))
print('Числа меньшие максимального числа из списка - ', l)


print('ЗАДАНИЕ 2')

q = [4, 7, -52, 11, -18, -27, -44, -11, 20, -17]
print('Список q =', q)
for i in q:
    for j in q:
        if i != j:
            if (i > 5) and (j > 5):
                print("Сумма чисел, которые больше 5 - ", i + j)