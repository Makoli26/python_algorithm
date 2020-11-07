# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843
BASE = 10

number = int(input('Введите целое число '))
result = 0
while number > 0:
    result = result * BASE + number % BASE
    number = number // BASE
print(result)
