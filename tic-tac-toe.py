def display_board():
    print('---------')
    print("|", board[0][2], board[1][2], board[2][2], "|")
    print("|", board[0][1], board[1][1], board[2][1], "|")
    print("|", board[0][0], board[1][0], board[2][0], "|")
    print('---------')


def check_coordinates():
    turn = 'O'
    count = 1
    for i in cells:
        while True:
            if count == 9:
                print("Draw")
                break
            else:
                coords = input('Enter the coordinates: ').split()
            if coords[0].isalpha() or coords[1].isalpha():
                print("You should enter numbers!")
            elif (int(coords[0]) < 1 or int(coords[0]) > 3) or (int(coords[1]) < 1 or int(coords[1]) > 3):
                print("Coordinates should be from 1 to 3!")
            elif board[int(coords[0]) - 1][int(coords[1]) - 1] != " ":
                print("Ocuupied")
            else:
                if turn == 'O':
                    turn = 'X'
                else:
                    turn = 'O'
                board[int(coords[0]) - 1][int(coords[1]) - 1] = turn

                count += 1
                display_board()
            break
        if count >= 5:
            if board[0][2] == board[1][2] == board[2][2] != ' ':  # across the top
                print(turn + " wins")
                break

            elif board[0][1] == board[1][1] == board[2][1] != ' ':  # across the middle
                # display_board()
                print(turn + " wins")
                break

            elif board[0][0] == board[1][0] == board[2][0] != ' ':  # across the bottom
                # display_board()
                print(turn + " wins")
                break

            elif board[0][2] == board[0][1] == board[0][0] != ' ':  # down the left side
                # display_board()
                print(turn + " wins")
                break

            elif board[1][2] == board[1][1] == board[1][0] != ' ':  # down the middle
                # display_board()
                print(turn + " wins")
                break

            elif board[2][2] == board[2][1] == board[2][0] != ' ':  # down the right side
                # display_board()
                print(turn + " wins")
                break

            elif board[2][2] == board[1][1] == board[0][0] != ' ':  # diagonal
                # display_board()
                print(turn + " wins")
                break

            elif board[0][2] == board[1][1] == board[2][0] != ' ':  # diagonal
                # display_board()
                print(turn + " wins")
                break


cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board = [
    [cells[6], cells[3], cells[0]],
    [cells[7], cells[4], cells[1]],
    [cells[8], cells[5], cells[2]]
]
display_board()
check_coordinates()
