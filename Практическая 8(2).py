print('ВАРИАНТ 2')
print('ЗАДАНИЕ 1')
n = 3
A = []
for i in range(n):
    B = []
    for i in range(n):
        B.append(int(input()))
    A.append(B)


for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

if ((A[0][0] + A[0][1] + A[0][2]) == (A[1][0] + A[1][1] + A[1][2])) and ((A[1][0] + A[1][1] + A[1][2]) == (A[2][0] + A[2][1] + A[2][2])):
    print('Матрица магическая')
else:
    print('Матрица не магическая')

print('ЗАДАНИЕ 2')
C = []
for i in range(n):
    D = []
    for i in range(n):
        D.append(int(input()))
    C.append(D)
print('Исходный массив')
for i in range(n):
    for j in range(n):
        print(C[i][j], end=' ')
    print()
a = C[0][0]
C[0][0] = C[0][2]
C[0][2] = a
a = C[1][0]
C[1][0] = C[1][2]
C[1][2] = a
a = C[2][0]
C[2][0] = C[2][2]
C[2][2] = a
print('Изменённый массив')
for i in range(n):
    for j in range(n):
        print(C[i][j], end=' ')
    print()
