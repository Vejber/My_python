# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def ten_to_two(number, count):
    result = []
    reverse = []
    for i in range(count+1):
        result.append(number % 2)
        number = number // 2
    # now reverse
    for i in range(len(result)//2 + len(result) % 2):
        temp = result[i]
        result[i] = result[count - i]
        result[count - i] = temp
    print(result)


number = int(input("Enter a number > "))
temp = number
number1 = number
count = 0
while number1 // 2 > 0:
    count = count + 1
    number1 = number1 // 2
number = temp
ten_to_two(number, count)
