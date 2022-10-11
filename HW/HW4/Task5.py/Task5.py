# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 2*x² + 4*x + 5
# 3*x² +10*x + 6
# Вывод: 5*x² + 14*x + 11

def str_to_int(list):
    result = []
    for i in list:
        if i == '*' or i == 'x²' or i == 'x' or i == '+':
            result.append(i)
        else:
            i = int(i)
            result.append(i)
    return result


def sum_list(list1, list2):
    list3 = []
    i = 0
    j = 0
    while j <= len(list2)-1:
        if list2[j] == '*' or list2[j] == 'x²' or list2[j] == 'x' or list2[j] == '+':
            list3.append(list1[j])
            j = j + 1
            i = i + 1
        else:
            list3.append(list1[i]+list2[j])
            j = j + 1
            i = i + 1
    print(list3)
    return list3


path = 'HW/HW4/Task5.py/polinom1.txt'
data = list((open(path, 'r')))
pol1 = data[0].split()
pol1 = str_to_int(pol1)
print(pol1)
path = 'HW/HW4/Task5.py/polinom2.txt'
data2 = list(open(path, 'r'))
pol2 = data2[0].split()
pol2 = str_to_int(pol2)
print(pol2)
data3 = sum_list(pol1, pol2)
data3 = str(data3)
with open('polinom3.txt', 'w') as p3:
    p3.write(data3)
