# Поиск контакта по имени


def find_contact(find_name):
    path = '/Users/zenecka/Desktop/Desktop/Разработка/My_python/HW/HW7/contacts.csv'
    data = open(path, 'r')
    for line in data:
        li = list(map(str, line.split()))
        if find_name in li:
            return (li)
    data.close()
    return ("There is no such contact.")
