# Добавить новый контакт

def add_person(id, name, surname, patronym, number, position, salary):
    with open('HW/HW8/workers.csv', 'a') as data:
        data.write(id)
        data.write('||')
        data.write(name)
        data.write('||')
        data.write(surname)
        data.write('||')
        data.write(patronym)
        data.write('||')
        data.write('+')
        data.write(number)
        data.write('||')
        data.write(position)
        data.write('||')
        data.write(salary)
        data.write('\n')
