# Нужно написать функцию, которая принимает три целых числа в качестве аргументов
# и определяет среднее значение (сумма трёх чисел делится на 3).

def average(number1: int, number2: int, number3: int):
    av = (number1 + number2 + number3) // 3
    return av

average1 = average(int(input("Enter number 1 > ")), int(input("Enter number 2 > ")), int(input("Enter number 3 > ")))
print("The average of the three numbers is {}.". format(average1))

