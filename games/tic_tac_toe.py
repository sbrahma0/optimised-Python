'''
TIC TAC TOE 2 HUMAN PLAYERS
'''
board = ['_','_','_',
        '_','_','_',
        '_','_','_']

current_player = "x"
game_on = True

# Similar to your NUMBAD LAYOUT
def display_board():
    print("\n")
    print(board[6]," | ",board[7]," | ",board[8])
    print(board[3]," | ",board[4]," | ",board[5])
    print(board[0]," | ",board[1]," | ",board[2])
    print("\n")

def switch_player():
    global current_player # for re-writing a global variable
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"
    return

# If the entered position is not valid or already taken
def validity_check(position):
    Flag1, Flag2 = False, False
    if position in [0,1,2,3,4,5,6,7,8]:
        Flag1 = True
    if board[position] == '_':
        Flag2 = True
    return Flag1, Flag2
    
def check_if_game_over():
    row_win_status = row_win()
    col_win_status = col_win()
    dia_win_status = dia_win()
    
    if row_win_status == True or col_win_status == True or dia_win_status == True:
        return "winner"
    elif '_' not in board:
        return "Tie"
    return

def row_win():
    row1 = board[6] == board[7] == board[8] != '_'
    row2 = board[3] == board[4] == board[5] != '_'
    row3 = board[0] == board[1] == board[2] != '_'
    
    if row1 or row2 or row3:
        return True
    return False

def col_win():
    col1 = board[6] == board[3] == board[0] != '_'
    col2 = board[7] == board[4] == board[1] != '_'
    col3 = board[8] == board[5] == board[2] != '_'
    
    if col1 or col2 or col3:
        return True
    return False

def dia_win():
    dia1 = board[6] == board[4] == board[2] != '_'
    dia2 = board[0] == board[4] == board[8] != '_'
    
    if dia1 or dia2:
        return True
    return False

def game_is_on():
    global board
    display_board()
    while game_on == True:
        print(current_player,"'s turn")
        position = input("Enter a position 1-9 as per numpad layout- ")
        position = int(position)-1
        Flag1, Flag2 = validity_check(position)
        while Flag1==False or Flag2==False:
            position = input("Please enter a position 1-9 as per numpad layout and position not taken- ")
            position = int(position)-1
            Flag1, Flag2 = validity_check(position)
        board[position] = current_player
        display_board()
        game_state = check_if_game_over()
        if game_state == "winner":
          print("Winner is - ",current_player)
          return
        if game_state == "Tie":
          print("The Game is Tied")
          return
        switch_player()

game_is_on()
    
