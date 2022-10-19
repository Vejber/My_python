# from pathlib import Path
# Добавить новый контакт

def add_contact(name, surname, patronym, number):
    with open('/Users/zenecka/Desktop/Desktop/Разработка/My_python/HW/HW7/contacts.csv', 'a') as data:
        data.write(name)
        data.write(' ')
        data.write(surname)
        data.write(' ')
        data.write(patronym)
        data.write(' || ')
        data.write('+')
        data.write(number)
        data.write('\n')
