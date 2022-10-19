from add_contact import add_contact as add
from find_contact import find_contact as find


action = int(input("Choose 1 for add OR 2 for seach > "))
if action == 1:
    name = str(input("Enter a name > "))
    surname = str(input("Enter a surname > "))
    patronym = str(input("Enter a patronym > "))
    number = str(input("Enter a phone number > "))
    add(name, surname, patronym, number)
elif action == 2:
    name = str(input("Enter a name > "))
    contact = find(name)
    print(contact)
else:
    print("Wrong command, try again.")
