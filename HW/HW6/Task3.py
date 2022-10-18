# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

a = int(input("Enter number 1 > "))
b = int(input("Enter number 2 > "))
def c(a, b): return a == b*b or b == a*a


print(c(a, b))
