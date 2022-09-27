# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def find_xy(num):
    if num == 1:
        print("x > 0; y > 0")
    elif num == 2:
        print("x < 0; y > 0")
    elif num == 3:
        print("x < 0; y < 0")
    else:
        print("x > 0; y < 0")


quarter = int(input("Enter quarter > "))
if 5 > quarter > 0:
    find_xy(quarter)
else:
    print("Incorrect quarter")
