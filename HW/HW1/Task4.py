# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check_true(x, y, z):
    print(not(x and y and z) == (not(x) or not(y) or not(z)))
    

x = int(input("Enter x > "))
y = int(input("Enter y > "))
z = int(input("Enter z > "))
check_true(x, y, z)