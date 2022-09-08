# Нужно написать функцию, которая будет определять количество десятков в указанном числе.

def Tens(number: int):
    if number < 0:
        number = number * -1
    number = number // 10
    return number


number = (int(input("Enter a number > ")))
how_many_tens = Tens(number)
print("The number of tens in {} is {}". format (number, how_many_tens))