# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними в 2D пространстве.

def space(x1, x2, y1, y2):
    s = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    s = round(s, 1)
    print(s)


x1 = float(input("Enter x1 > "))
y1 = float(input("Enter y1 > "))
x2 = float(input("Enter x2 > "))
y2 = float(input("Enter y2 > "))
space(x1, x2, y1, y2)
