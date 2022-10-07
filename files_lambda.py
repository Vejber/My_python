numbers = ['1', '2', '3', '5', '8', '15', '23', '38']
data = open('lambda.txt', 'w')
data.writelines(numbers)
data.close()  # обязательно завершить процесс

# doesnt work:
# def f(i):
#     return i**2


# path = 'lambda.txt'
# data = open(path, 'r')
# out = []
# for line in data:
#     out = [(i, i**2) for i in numbers if i % 2 == 0]
#     print(out)
# data.close()


# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# works from lecture:
# https://gb.ru/lessons/269978
# 32 minute
