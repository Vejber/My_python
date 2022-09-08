# Нужно написать функцию, которая определяет время года (Зима, Весна, Лето, Осень) указанного номера месяца (от 1 до 12). 
# При попытке передачи неверного номера, программа должна вернуть сообщение об ошибке: Неверный номер месяца.

def season(number: int):
    if number > 0 and number < 3 or number == 12:
        return "winter"
    if number > 2 and number < 6:
        return "spring"
    if number > 5 and number < 9:
        return "summer"
    if number > 8 and number < 12:
        return "fall"
    else:
        return "Incorrect number of the month"

month = season(int(input("Enter month number > ")))
print(month)
     