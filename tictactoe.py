board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game = False


def tpel():
    print("COORDINATES")
    print("| 0 | 1 | 2 |")
    print("|---|---|---|")
    print("| 3 | 4 | 5 |")
    print("|---|---|---|")
    print("| 6 | 7 | 8 |")
    print("-" * 100)
    print("DESK")
    print(" -----------")
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("|---|---|---|")
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print("|---|---|---|")
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
    print(" -----------")


def win(board):
    win_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for x in win_combos:
        if board[x[0]] == board[x[1]] == board[x[2]] != " ":
            if board[x[0]] == "X":
                print("Game is over\nPlayer 1 wins")
            else:
                print("game is over\nPlayer 2 wins")
            return True
    count = 0
    for x in range(9):
        if board[x] != " ":
            count += 1
        if count == 9:
            print("Game is over\nIts TIE")
            return True


def print_for_file():
    return " -----------\n", "| {} | {} | {} |\n".format(board[0], board[1], board[2]), "|---|---|---|\n", \
           "| {} | {} | {} |\n".format(board[3], board[4], board[5]), "|---|---|---|\n", \
           "| {} | {} | {} |\n".format(board[6], board[7], board[8]), " -----------\n"


def print_in_file(a):
    file_name = "tictactoe"
    with open(file_name + ".txt", "w") as file:
        for x in a:
            file.writelines(x)


tpel()
while not game:

    while True:
        inp1 = input("Enter Coordinate Player 1: ")
        try:
            inp1 = int(inp1)
            if inp1 in range(0, 9):
                if board[inp1] != "X" and board[inp1] != "O":
                    board[inp1] = "X"
                    tpel()
                    break
                else:
                    print("Wrong place. Try again ")
            else:
                print("\nThat's not on the board. Try again ")
        except ValueError:
            print("\nThat's not a number. Try again ")

    game = win(board)
    if game is True:
        a = print_for_file()
        print_in_file(a)
        break

    while True:
        inp2 = input("Enter Coordinate Player 2: ")
        try:
            inp2 = int(inp2)
            if inp2 in range(0, 9):
                if board[inp2] != "O" and board[inp2] != "X":
                    board[inp2] = "O"
                    tpel()
                    break
                else:
                    print("Wrong place. Try again ")
            else:
                print("\nThat's not on the board. Try again ")
        except ValueError:
            print("\nThat's not a number. Try again ")

    game = win(board)
    if game is True:
        a = print_for_file()
        print_in_file(a)
        break


