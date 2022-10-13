# Создайте программу для игры в ""Крестики-нолики"".

# Function to print the Tic-Tac-Toe Design


def mytictactoe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")


val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mytictactoe(val)
for i in val:
    n1 = int(input("Enter the position to put an X at: "))
    if (1 <= n1 <= 9):
        val[n1-1] = 'X'
        mytictactoe(val)
    else:
        print("The position should be from 1 to 9")
    n2 = int(input("Enter the position to put an O at: "))
    if (1 <= n2 <= 9):
        val[n2-1] = 'O'
        mytictactoe(val)
    else:
        print("The position should be from 1 to 9")

    if ((val[0] == 'X' and val[1] == 'X' and val[2] == 'X')
        or (val[0] == 'O' and val[1] == 'O' and val[2] == 'O')
        or (val[3] == 'X' and val[4] == 'X' and val[5] == 'X')
        or (val[3] == 'O' and val[4] == 'O' and val[5] == 'O')
        or (val[6] == 'X' and val[7] == 'X' and val[8] == 'X')
        or (val[6] == 'O' and val[7] == 'O' and val[8] == 'O')
        or (val[0] == 'X' and val[3] == 'X' and val[6] == 'X')
        or (val[0] == 'O' and val[3] == 'O' and val[6] == 'O')
        or (val[1] == 'X' and val[4] == 'X' and val[7] == 'X')
        or (val[1] == 'O' and val[4] == 'O' and val[7] == 'O')
        or (val[2] == 'X' and val[5] == 'X' and val[8] == 'X')
        or (val[2] == 'O' and val[5] == 'O' and val[8] == 'O')
        or (val[0] == 'X' and val[4] == 'X' and val[8] == 'X')
        or (val[0] == 'O' and val[4] == 'O' and val[8] == 'O')
        or (val[2] == 'X' and val[4] == 'X' and val[6] == 'X')
            or (val[2] == 'O' and val[4] == 'O' and val[6] == 'O')):
        print("Game over.")
        break
