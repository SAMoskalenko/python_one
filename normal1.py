num = int(input('Введите число больше нуля но мельше 10: '))
while num <= 0 or num >= 10:
    print('Не верное число!')
    num = int(input('Введите число больше нуля но мельше 10: '))
print(num ** 2)

a = int(input('ввдите число: '))
b = int(input('ввдите число: '))

a, b = b, a

print(a)
print(b)