# li = [x for x in range(1, 20)]  # x from 1 to 19
# li = list(map(lambda x: x+10, li))
# # map(function, data) -  do x+10 for each x from list
# print(li)

data = list(map(int, input().split()))
# take input, split it with backspace, turn it into int
print(data)
