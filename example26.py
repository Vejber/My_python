# Нужно написать программу, которая запрашивает у пользователя три строки. 
# Если эти строки "раз", "два", "три" или "1", "2", "3", то программа должна вывести Ёлочка, гори, иначе Не гори.




def string_check(string1, string2, string3):
    string1 = string1.lower()
    string2 = string2.lower()
    string3 = string3.lower()
    if ((string1 == "раз" or string1 == "1") and (string2 == "два" or string2 == "2") and (string3 == "три" or string3 == "3")):
        print("Ёлочка гори")
    else:
        print("Не гори")


happy = (input(str("Enter a string > ")))
new = (input(str("Enter a string > ")))
year = (input(str("Enter a string > ")))
string_check(happy, new, year)