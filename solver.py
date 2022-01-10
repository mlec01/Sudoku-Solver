def print_board(board):
    ''' Prints a visual of the sudoku board'''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("_____________________")
        else:
            print("- - - - - - - - - - -")
        for j in range(len(board[i])):
            if j % 3 == 2 and j != 8:
                print(str(board[i][j]) + " | ", end="")
            else:
                print(str(board[i][j]) + " ", end="")

        print("")


def find_empty(board):
    ''' Finds the next empty spot on the board and returns the position of the spot as a tuple'''
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid_num(number, position, board):
    ''' Checks to see if a number is valid in a certain spot'''
    row, col = position

    # Check row to see if number works
    for j in range(len(board[row])):
        if board[row][j] == number and j != col:
            return False

    # Check column to see if number works
    for i in range(len(board)):
        if board[i][col] == number and i != row:
            return False

    # Check box to see if number works
    box_pos_x = row // 3
    box_pos_y = col // 3

    box_pos_x_start = box_pos_x * 3
    box_pos_y_start = box_pos_y * 3

    for i in range(box_pos_x_start, box_pos_x_start + 3):
        for j in range(box_pos_y_start, box_pos_y_start + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


def solve_board(board):
    ''' Solves the sudoku board '''

    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        valid = valid_num(num, empty, board)
        if valid:
            board[row][col] = num

            if solve_board(board):
                return True
            else:
                board[row][col] = 0

    return False


def launcher():
    ''' Launches the sudoku solver '''

    print("Please enter the numbers of the sudoku board with a new line to separate the rows and spaces in between the numbers of the rows")
    print("Please enter zeroes as empty spaces")
    n = int(input("Enter the size of sudoku board: "))
    print("Enter sudoku board: \n ")

    board = [[int(num) for num in input().split()] for row in range(n)]

    print("\n\n")
    print("Sudoku Board")
    print_board(board)
    print("\n\n")
    solve_board(board)
    print("Solution")
    print_board(board)


launcher()
