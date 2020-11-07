#Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).



number = int(input('Введите целое число: '))
even_number = 0
odd_number = 0
while number > 0:
    if number % 2 == 0:
        even_number +=1
    else:
        odd_number +=1
    number = number // 10
print(f'четные числа: {even_number}, нечетные числа {odd_number}')