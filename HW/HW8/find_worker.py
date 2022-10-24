# Поиск контакта, изменение


def find_worker(find_name):
    path = 'HW/HW8/workers.csv'
    data = open(path, 'r')
    for line in data:
        li = list(map(str, line.split('||')))
        if find_name in li:
            print(li)
            return (li)
    data.close()
    return ("There is no such employee.")


def edit_worker(id):
    path = 'HW/HW8/workers.csv'
    data = open(path, 'r')
    for line in data:
        li = list(map(str, line.split('||')))
        print(li)

        if id not in li:
            # continue
            with open(path, 'w') as new_data:
                new_data.write(line)
        elif id in li:
            j = int(input("Enter 1 to edit name, OR 2 to edit surname OR 3 to edit patronym, OR 4 to edit phone number, OR 5 to edit position, OR 6 to edit salary > "))
            li[j] = str(input("Enter a new value > "))
            li = ('||'.join(map(str, li)))
            print(li)
            with open(path, 'w') as new_data:
                new_data.write(li)
    data.close()
    return ("All done.")
