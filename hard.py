name = input('Введите Имя и Фамилилю: ')
age = int(input('Возраст: '))
weight = int(input('Вес: '))

if age < 30 and 50 < weight < 120:
    print(name, ',', age, 'год, вес', weight, '- хорошее состояние')
elif 40 > age > 30 and (50 > weight or 120 < weight):
    print(name, ',', age, 'год, вес', weight, '- следует заняться собой')
elif age > 40 and (50 > weight or 120 < weight):
    print(name, ',', age, 'год, вес', weight, '- следует обратится к врачу!')
else:
    print(name, ',', age, 'год, вес', weight, '- зачем вы здесь?')