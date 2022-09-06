# Нужно написать программу, которая запрашивает у пользователя два целых числа (координаты точки на плоскости) и определяет в какой четверти находится точка. 
# Программа должна вывести номер четверти: I, II, III, IV.

x = int(input("Введите x > "))
y = int(input("Введите y > "))
if x > 0 and y > 0:
    print("I")
if x < 0 and y > 0:
    print("II")
if x < 0 and y < 0:
    print("III")
if x > 0 and y < 0:
    print("IV")
elif x == 0 or y == 0:
    print("Impossible to find.")