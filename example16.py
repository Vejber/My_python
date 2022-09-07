# Нужно переписать программу - Консольный калькулятор. Весь алгоритм нужно добавить в цикл, 
# чтобы у пользователя была возможность использовать доступные команды постоянно, пока он сам не прервёт выполнение программы.

while 1:
    number_1 = int(input("Введите первое число > "))
    number_2 = int(input("Введите второе число > "))
    print("Я могу выполнить: [1] Сложение, [2] Вычитание, [3] Умножение, [4] Деление, [5] Остановить калькулятор.")
    to_do_num = int(input("Введите число в соответствии с командой > "))
    if to_do_num == 1:
      print(number_1 + number_2)
    if to_do_num == 2:
      print(number_1 - number_2)
    if to_do_num == 3:
      print(number_1 * number_2)
    if to_do_num == 4:
     print(number_1 // number_2)
    elif to_do_num != 1 and to_do_num != 2 and to_do_num != 3 and to_do_num != 4 and to_do_num != 5:
     print("Нет такой команды.")
    if to_do_num == 5:
     break

