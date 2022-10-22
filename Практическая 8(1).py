print('ВАРИАНТ 13')
print('ЗАДАНИЕ 1')
A = []
n = 3
min = 99999999
for i in range(n):
    B = []
    for i in range(n):
        B.append(int(input()))
    A.append(B)
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
for i in range(n):
    if min > A[0][i]:
        min = A[0][i]
print('Минимальное число из 1 строки', min)
min = 999999
for i in range(n):
    if min > A[1][i]:
        min = A[1][i]
print('Минимальное число из 2 строки', min)
min = 999999
for i in range(n):
    if min > A[2][i]:
        min = A[2][i]
print('Минимальное число из 3 строки', min)

print('ЗАДАНИЕ 2')
C = []
n = 3
for i in range(n):
    D = []
    for i in range(n):
        D.append(int(input()))
    C.append(D)
print('Начальный массив')
for i in range(n):
    for j in range(n):
        print(C[i][j], end=' ')
    print()
minimum = [0, 0, 9999999]
maximum = [0, 0, -9999999]

for i in range(len(C)):
    for j in range(len(C)):
        if C[i][j] > maximum[2]:
            maximum[0] = i
            maximum[1] = j
            maximum[2] = C[i][j]

for i in range(len(C)):
    for j in range(len(C)):
        if C[i][j] < minimum[2]:
            minimum[0] = i
            minimum[1] = j
            minimum[2] = C[i][j]

C[maximum[0]][maximum[1]] = minimum[2]
C[minimum[0]][minimum[1]] = maximum[2]

print('Изменённый массив')
for i in range(n):
    for j in range(n):
        print(C[i][j], end=' ')
    print()