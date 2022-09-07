# Нужно написать программу, которая запрашивает у пользователя два целых (n1, n2) числа и выводит сумму чисел от n1 до n2.

number_1 = int(input("Enter number 1 > "))
number_2 = int(input("Enter number 2 > "))
sum = 0
if number_1 > number_2:
    temp = number_2
    number_2 = number_1
    number_1 = temp
while number_1 <= number_2:
    sum = sum + number_1
    number_1 = number_1 + 1
print(sum)

