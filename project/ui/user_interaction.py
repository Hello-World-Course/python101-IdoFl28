# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
name = None
board_size = None
number_of_mines = None
faulty = False

name_input = input("Hello, whats your name: \n>")
if len(name_input) > 2:
    name = name_input
else:
    print("Your name is too short!")
    faulty = True

if not faulty:
    board_size_input = int(input(f"{name}, please choose board size: "))
    if 0 < board_size_input < 26:
        board_size = board_size_input
    else:
        print(f"{name}, you have entered illegal board size")
        faulty = True


if not faulty:
    number_of_mines_input = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate: "))
    if 0 < number_of_mines_input <= (board_size / 2):
        number_of_mines = number_of_mines_input
    else:
        print(f"{name}, you have entered illegal number of mines")
        faulty = True
print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}")
