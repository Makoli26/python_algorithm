a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if b < a < c or c < a < b:
    print('Среднее число', a)
elif a < b < c or c < a < b:
    print('Среднее число ', b)
else:
    print('Среднее число ', c)