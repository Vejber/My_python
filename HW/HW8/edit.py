
# def edit(list):
#     path = 'HW/HW8/workers.csv'
#     list = ('||'.join(map(str, list)))
#     with open(path, 'w') as data:
#         data.write(list)
#     return list


# for line in data:
#     data.writelines(line)

def edit(id):
    path = 'HW/HW8/workers.csv'
    with open(path, 'r') as data:
        # with open(data, 'w') as data:
        for line in data:
            li = list(map(str, line.split('||')))
            if id not in li:
                li = ('||'.join(map(str, li)))
                line = line.replace(line, li)
    #             li = ('||'.join(map(str, li)))
    #             with open(path, 'r') as data:
    #                 for line in data:
    #                     if line == li:
    #                         line = line.replace(line, li)
    #                         data.write(line)
    # #          with open("file1.txt", "wt") as file:
    # # x = x.replace("gode","God")
    #     # fin.write(x)
    #                         # with open(line, 'w') as line:
    #                         # li = list(map(str, line.split('||')))
    #                         # li = ('||'.join(map(str, li)))
    #                         # line.write(li)
    #                     else:
    #                         continue
                li = list(map(str, li.split('||')))
            elif id in li:
                j = int(input(
                    "Enter 1 to edit name, OR 2 to edit surname OR 3 to edit patronym, OR 4 to edit phone number, OR 5 to edit position, OR 6 to edit salary > "))
                with open(path, 'r') as data:
                    # with open(data, 'w') as data:
                    for line in data:
                        # li = list(map(str, line.split('||')))
                        li = ('||'.join(map(str, li)))
                        if line != li:
                            li = list(map(str, li.split('||')))
                            continue
                        elif line == li:
                            li = list(map(str, line.split('||')))
                            # li = list(map(str, line.split('||')))
                            li[j] = str(input("Enter a new value > "))
                            li = ('||'.join(map(str, li)))
                            line = line.replace(line, li)
                            li = list(map(str, li.split('||')))
                            with open(path, 'w') as data:
                                data.writelines(line)
                            # with open(line, 'w') as line:
                            #     line.write(li)

            # list = ('||'.join(map(str, list)))
    data.close()
    return ("All done.")

    # with open(path, 'w') as data:
    #     data.write(list)
    # return list
