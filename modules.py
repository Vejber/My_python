# Чтобы повторно использовать функцию в другом модуле можно воспользоваться выражением from ... import ...

# Внимание: модуль должен находиться либо в том же каталоге, что и программа, в которую он импортируется, либо в одном из каталогов, указанных в sys.path.

# from module import multiplication

# print(multiplication(2, 3))
# Выражение from ... import ... можно дословно перевести как "из модуля импортировать функцию".

 

# Из модуля можно импортировать сразу несколько функций.

# from module import multiplication, power

# print(multiplication(2, 3))

# print(power(2, 3))
 

# Или импортировать сразу всё.

# from module import *

# print(multiplication(2, 3))

# print(power(2, 3))
 

# В общем случае следует избегать использования выражения from ... import ... и вместо него использовать оператор import, т.к. при использовании нескольких модулей может возникнуть конфликт имён. Например, в проекте подключены два модуля, в обоих модулях есть функция с названием multiplication. Названия функций одинаковы, но алгоритмы разные. Возникает конфликт имён, какой алгоритм нужно выполнить.

# import module

# print(module.multiplication(2, 3))

# print(module.power(2, 3))
# В этом примере конфликта имён не будет, т.к. перед названием функции указывается название модуля, откуда импортируется команда.

 

# Модулю можно присвоить синоним с помощью оператора as (как) и обращаться к функциям уже через синоним.

# import module as m

# print(m.multiplication(2, 3))

# print(m.power(2, 3))

# распространенные модули: https://stepik.org/lesson/733331/step/1?unit=734854


def multiplication(number_1: int, number_2: int):
    # """
    # Функция умножает два числа не используя оператор умножения
    # Пример: 2 * 3 = 2 + 2 + 2 = 3
    # """
    result = 0
    while number_2 > 0:
        result += number_1
        number_2 -= 1
    return result


def power(number, exponent):
    """
    Функция возводит число в степень
    Пример: 2 ^ 3 = 2 * 2 * 2 = 8
    """
    result = 1
    while exponent > 0:
        result = multiplication(result, number)
        exponent -= 1
    return result

def string_check(string): 
    string = string.lower() #делает регистр строки нижним
    if (string == "тик"):
        print("ТАК")
    elif(string == "так"):
        print("ТИК")
    else:
        print("Часики")


# string = (input(str("Enter a string > ")))
# string_check(string)