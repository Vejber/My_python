# неупорядоченные коллекци произвольных объектов с доступом по ключу
# словари

dictionary = {}
dictionary = \
    {
        'up': "^",
        'left': "<",
        'down': "v",
        'right': ">"
    }
print(dictionary)
print(dictionary['left'])

# print keys:
for k in dictionary.keys():
    print(k)

# print values:
for k in dictionary.values():
    print(k)
# or
for k in dictionary:
    print(k)