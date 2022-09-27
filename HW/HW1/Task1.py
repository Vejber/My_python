#  Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

def day_week(num):
    if num > 5:
        print("it's a weekend day")
    else:
        print("it's a weekday")



number = int(input("Enter the number of the day > "))
if number > 0 and number < 8:
    day_week(number)
else:
    print("Incorrect day")