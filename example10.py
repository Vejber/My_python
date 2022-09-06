# Нужно написать программу, которая загадывает число или загадку и выводит сообщение: Угадал или Не угадал.

x = int(input("I have a number from 1 to 3 in mind. Try to guess it. Enter your number > "))
y = 3
if x == y:
    print("You guessed the number")
else:
    print("Sorry, you did not guess the number")