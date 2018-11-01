def dimension():
    while True:
        try:
            dimension = int(input("Input dimension of the board: "))
            if dimension >= 3:
                return dimension
            else:
                print("Please entar a dimension greater than or equal to 3")
        except: 
            print("Invalid input!")

def create_board(width):
    board = []
    line = []
    for i in range(width):
        for k in range(1,width+1):
            line.append(str(k+i*dime))
        board.append(line)
        line = []
    return board

def print_board(board_list):
    for value in board_list:
        for item in value:
            print("{:>5}".format(item), end = "")
        print("")

def input_position(board_list):
    while True:
        position = (input("{} position: ".format(X_O(counter))))
        for a_list in board_list:
            if position in a_list:
                return position
        print("Illegal move!")

def play(board_list):
    position = input_position(board_list)
    length = len(board_list)
    for i in range(length):
        for k in range(length):
            if board_list[i][k] == position:
                board_list[i][k] = X_O(counter)
               
def X_O(counter):
    has_turn = "X"
    if counter % 2 == 0:
        has_turn = "O"
    return has_turn

def game_on(board):
    print_board(main_list)
    play(main_list)

def make_vertical(i,a_list):
    verticalX = []
    verticalO = []
    for row in a_list:
        verticalX.append(row[i])
        verticalO.append(row[i])
    for i in range(len(a_list)):
        if "X" in verticalX:
            verticalX.remove("X")
    for i in range(len(a_list)):
        if "O" in verticalO:
            verticalO.remove("O")
    return verticalX,verticalO

def make_horizontal(row):
    horizontalX = []
    horizontalO = []
    for item in row:
        horizontalX.append(item)
        horizontalO.append(item)
    for i in range(len(main_list)):
        if "X" in horizontalX:
            horizontalX.remove("X")
    for i in range(len(main_list)):
        if "O" in horizontalO:
            horizontalO.remove("O")
    return horizontalX,horizontalO

def make_diagonal1(a_list): 
    diagonal1X = []
    diagonal1O = []
    for i in range(len(a_list)):
        diagonal1X.append(a_list[i][i])
        diagonal1O.append(a_list[i][i])
    for i in range(len(a_list)):
        if "X" in diagonal1X:
            diagonal1X.remove("X")
    for i in range(len(a_list)):
        if "O" in diagonal1O:
            diagonal1O.remove("O")
    return diagonal1X,diagonal1O

def make_diagonal2(a_list):
    diagonal2X = []
    diagonal2O = []
    for i in range(1,len(a_list)+1):
        diagonal2X.append(a_list[i-1][-i])
        diagonal2O.append(a_list[i-1][-i])
    for i in range(len(a_list)):
        if "X" in diagonal2X:
            diagonal2X.remove("X")
    for i in range(len(a_list)):
        if "O" in diagonal2O:
            diagonal2O.remove("O")
    return diagonal2X,diagonal2O

def game_over(board_list):
    for row in board_list:
        horizontalX,horizontalO = make_horizontal(row)     
        if horizontalX == []:       
            return False, "X"
        if horizontalO == []:
            return False, "O"
    for i in range(len(board_list)):
        verticalX,verticalO = make_vertical(i,board_list)
        if verticalX == []:
            return False, "X"
        if verticalO == []:
            return False, "O"
    diagonal1X,diagonal1O = make_diagonal1(board_list)
    if diagonal1X == []:
        return False, "X"
    if diagonal1O == []:
        return False, "O"
    diagonal2X,diagonal2O = make_diagonal2(board_list)
    if diagonal2X == [] or diagonal2O == []:
        return False, "X"
    if diagonal2O == []:
        return False, "O"
    return True, ""

counter = 1
play_counter = 0
dime = dimension()
main_list = create_board(dime)
game = True
winner = ""
while game and play_counter < dime**2:
    game_on(main_list)
    counter += 1
    game, winner = game_over(main_list)
    if winner:
        print_board(main_list)
        print("Winner is: {}".format(winner))
    play_counter += 1

if play_counter == dime**2:
    print_board(main_list)
    print("Draw!")