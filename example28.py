# Нужно написать программу, которая запрашивает у пользователя температуру в градусах Цельсия и выводит 
# Холодно, если температура меньше 15.5, Жарко, если температура больше 28 и Нормально во всех остальных случаях.

def judgement(number):
    if number < 15.5:
        print("It's cold")
    if number > 28:
        print("It's hot")
    else:
        print("It's ok")



degree = (float(input("How many degrees are outside? > ")))
judgement(degree)