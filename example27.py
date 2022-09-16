# Нужно написать программу, которая запрашивает у пользователя строку и выводит ТАК, если строка ТИК и ТИК, если строка ТАК

def string_check(string):
    string = string.lower()
    if (string == "тик"):
        print("ТАК")
    elif(string == "так"):
        print("ТИК")
    else:
        print("Часики")


string = (input(str("Enter a string > ")))
string_check(string)