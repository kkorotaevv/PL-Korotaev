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
print('ЗАДАНИЕ 3')
def f():
    s = [int(i) for i in input('Введите данные: ').split() if int(i)]
    print(*s[::2])
f()
