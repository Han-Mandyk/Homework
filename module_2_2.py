first = int(input('Введи первое число: '))
second = int(input('Введи второе число: '))
third = int(input('Введи третье число: '))

if first == second and second == third:
    print('Есть 3 одинаковых числа')
elif first == second or second == third or first == third:
    print('Есть 2 одинаковых числа')
else:
    print('Нет одинаковых числа')