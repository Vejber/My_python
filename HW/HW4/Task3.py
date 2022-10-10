# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def repeat_check(data):
    li = []
    for i in data:
        if data.count(i) == 1:  # .count - counts the number of such elements
            li.append(i)
    print(li)


print("Enter the elements: ")
data = list(map(int, input().split()))
print(data)
repeat_check(data)
