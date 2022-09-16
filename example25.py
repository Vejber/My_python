# Нужно написать программу, которая запрашивает у пользователя строку и
# если это строка "Python" или "Алгоритм", то программа должна вывести Да, в противном случае программа должна вывести Нет.

def string_check(string):
    if string == "Python" or string == "Алгоритм":
        print("Yes")
    else:
        print("No")


string = (input(str("Enter a string > ")))
string_check(string)
