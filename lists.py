list1 = [1, 2, 3, 4, 5]
list1.pop()  # извлекает последний элемент
list1.pop(1)  # извлекает элемент по индексу
list1.insert(2, 11)  # на индекс 2 вставляем в лист значение 11
list1.append(11)  # на последний индекс вставляем в лист значение 11

# ways to fill list:
# primitive:
# list = []
# for i in range(1, 101):
#     list.append(i)
# print(list)

# amateur:
# list = [i for i in range(1, 21)]
# print(list)

# with condition:
# list = [i for i in range(1, 21) if i % 2 == 0]
# print(list)

# with tuples create pairs for each element:
# list = [(i, i) for i in range(1, 21) if i % 2 == 0]
# print(list)

# with function:


def f(i):
    return i**3


list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list)
