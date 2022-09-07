# Нужно написать программу, которая запрашивает у пользователя одно целое число (n) и выводит все числа от 1 до n не кратные 3.

number = int(input("Enter a number > "))
i = 1
if number > 0:
    while i <= number:
        while i % 3 != 0:
            print(i)
            break
        i = i + 1
if number < 0:
    while i >= number:
        while i % 3 != 0:
            print(i)
            break
        i = i - 1
elif number == 0:
    print(number)
    print(i)
