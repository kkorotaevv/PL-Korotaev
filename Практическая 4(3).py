n = int(input())
fact = 1
s = 0
for i in range(1, n + 1):
    fact *= i
    s += fact
print(s)