print('БЛОК А')
print('ЗАДАНИЕ 1')
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

def fuct(a, b):
    return a**b/fac(b)
x = int(input('Введите число x - '))
n = int(input('Введите число n - '))
print(fuct(x, n))
print('БЛОК Б')
print('ЗАДАНИЕ 1')
def str():
    a = int(input('Введите число '))
    if a == 0:
        return 1
    return max(a, str())
print(str())