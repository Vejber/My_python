from add_person import add_person as add
from find_worker import find_worker as find
from find_worker import edit_worker as edit


action = int(input("Choose 1 for add OR 2 for seach OR 3 for edit> "))
if action == 1:
    id = str(input("Enter id > "))
    name = str(input("Enter a name > "))
    surname = str(input("Enter a surname > "))
    patronym = str(input("Enter a patronym > "))
    number = str(input("Enter a phone number > "))
    position = str(input("Enter a position > "))
    salary = str(input("Enter a salary > "))
    add(id, name, surname, patronym, number, position, salary)
elif action == 2:
    name = str(input("Enter a name > "))
    contact = find(name)
    print(contact)
elif action == 3:
    find_id = str(input("Enter id > "))
    contact = edit(find_id)
    print(contact)
else:
    print("Wrong command, try again.")
