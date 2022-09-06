# Нужно написать программу, которая запрашивает у пользователя целое число и выводит текст по примеру.

# Sample Input:

# 37
# Sample Output:

# После числа 37 идёт число 38, а перед числом 37 идёт число 36. 

number_1 = int(input("Введите число > "))
number_0 = number_1 - 1
number_2 = number_1 + 1
print("After number {} goes number {}, and before number {} goes number {}.". 
format(number_1, number_2, number_1, number_0))