f = int(input("Введите значение f "))
v = int(input("Введите значение v "))
if (f < 4) and (v > 6):
    S = f + v
elif v < 6:
    k = int(input("Введите значение k "))
    S = k ** 2
else:
    S = 2 * v
print('S =', S)