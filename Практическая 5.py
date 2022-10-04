text = input("Введите строку: ")
k = 0
for i in text:
    if i == 'т':
        k += 1
print('Количество букв "т", в строке - ', k)