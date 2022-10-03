# Реализуйте алгоритм перемешивания списка.
import random
list = []
for i in range(1,5):
    list.append(random.randint(-5, 5))
print(list)
random.shuffle(list)
print(list)