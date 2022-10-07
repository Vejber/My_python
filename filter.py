# filter function filters elements by function:
# f(x) -> x - even
# filter(f, [1,2,3,4,5,6]) -> [2,4,6]

data = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data))
print(res)
