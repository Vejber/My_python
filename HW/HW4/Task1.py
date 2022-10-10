# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from random import uniform

num = float(input("Enter a number > "))
d = uniform(10**(-1), 10**(-10))
d = d-int(d)
print(d)
print("Enter the digits after the point in the number shown above ^ ")
data = list(map(int, input().split()))
print(data)
num = round(num, len(data))
print(num)
