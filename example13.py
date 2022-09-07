# Нужно написать программу, которая запрашивает у пользователя одно целое число (n) и выводит все числа от 1 до n с шагом 2.

number = int(input("Enter a number > "))  
i = 1
if number > 0:
    while i <= number:  
        print(i)  
        i = i + 2  
if number < 0:
    while i >= number:
        print(i)
        i = i - 2
elif number == 0:
    print(i)
