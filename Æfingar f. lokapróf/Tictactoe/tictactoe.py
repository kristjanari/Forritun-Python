def get_dimension():
    while True:
        try:
            return int(input("Input dimension of the board: "))
        except:
            print("Please enter an integer!")

def create_board(size):
    board =[]
    for i in range(size):
        row = []
        for j in range(1,size+1):
            row.append(j+i*size)
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for num in row:
            print("{:>5}".format(num), end = "")
        print()

def has_turn(plays):
    if plays % 2 == 0:
        return "X"
    else:
        return "O"

def get_position(turn, board):
    while True:
        position = input("{} position: ".format(turn))
        try:
            position = int(position)
        except:
            print("Please enter an integer!") 
            continue
        if (position < 1 or position > len(board)**2):
            print("Position out of range!")
            continue
        elif board[(position-1)//len(board)][position%len(board) - 1] != position:
            print("Illegal move!")
            continue
        return position

def get_and_mark_position(plays, board):
    turn = has_turn(plays)
    position = get_position(turn, board)
    for row in board:
        for index, num in enumerate(row):
            if num == position:
                row[index] = turn

def win(letter, board, a_list):
    if a_list == [letter for i in range(len(board))]:
        return True
    return False

def horizontal_win(letter, board):
    for row in board:
        if win(letter, board, row):
            return True
    return False
    
def vertical_win(letter, board):
    for i in range(len(board)):
        vertical = []
        for row in board:
            vertical.append(row[i])
        if win(letter, board, vertical):
            return True
    return False
        
def diagonal_win(letter, board):
    diagonal1 = []
    diagonal2  = []
    for i in range(len(board)):
        diagonal1.append(board[i][i])
    if win(letter, board, diagonal1):
        return True
    for i in range(1, len(board)+1):
        diagonal2.append(board[i-1][-i])
    if win(letter, board, diagonal2):
        return True
    return False

def is_winner(letter, board):
    if (horizontal_win(letter, board) or vertical_win(letter, board) or diagonal_win(letter, board)):
        return True, letter
    else:
        return False, ""
                
def main():
    dimension = get_dimension()
    board = create_board(dimension)
    print_board(board)
    plays = 0
    rounds = dimension**2
    game_won = False
    while game_won != True and rounds > 0:
        get_and_mark_position(plays, board)
        game_won, winner = is_winner(has_turn(plays), board)
        plays += 1
        rounds -= 1
        print_board(board)
    if winner:
        print("Winner is:", winner)
    else:
        print("Draw!")

main()