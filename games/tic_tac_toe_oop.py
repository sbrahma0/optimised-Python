#Objective: Coding Tic Tac Toe from scratch
'''
This class is responsible for initiating a board and display the board
'''
class Board():
    def __init__(self):
        self.board = ['_', '_', '_',
                      '_', '_', '_',
                      '_', '_', '_']

    # Similar to your NUMBAD LAYOUT
    def display_board(self):
        print("\n")
        print(self.board[6], " | ", self.board[7], " | ", self.board[8])
        print(self.board[3], " | ", self.board[4], " | ", self.board[5])
        print(self.board[0], " | ", self.board[1], " | ", self.board[2])
        print("\n")

'''
Handles the validation check like- 
1. whether the number entered is with in 1-9
2. The entered position is taken or not
3. Is there a Winner
4. Is the Game Tied
'''
class validation(object):
    def __init__(self,board):
        self.board = board

    def check_if_game_over(self):
        row_win_status = self.row_win()
        col_win_status = self.col_win()
        dia_win_status = self.dia_win()

        if row_win_status == True or col_win_status == True or dia_win_status == True:
            return "winner"
        elif '_' not in self.board.board:
            return "Tie"
        return

    # If the entered position is not valid or already taken
    def validity_check(self, position):
        Flag1, Flag2 = False, False
        if position in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            Flag1 = True
        if position < 9 and position >-1 and self.board.board[position] == '_':
            Flag2 = True
        return Flag1, Flag2


    def row_win(self):
        row1 = self.board.board[6] == self.board.board[7] == self.board.board[8] != '_'
        row2 = self.board.board[3] == self.board.board[4] == self.board.board[5] != '_'
        row3 = self.board.board[0] == self.board.board[1] == self.board.board[2] != '_'

        if row1 or row2 or row3:
            return True
        return False


    def col_win(self):
        col1 = self.board.board[6] == self.board.board[3] == self.board.board[0] != '_'
        col2 = self.board.board[7] == self.board.board[4] == self.board.board[1] != '_'
        col3 = self.board.board[8] == self.board.board[5] == self.board.board[2] != '_'

        if col1 or col2 or col3:
            return True
        return False


    def dia_win(self):
        dia1 = self.board.board[6] == self.board.board[4] == self.board.board[2] != '_'
        dia2 = self.board.board[0] == self.board.board[4] == self.board.board[8] != '_'

        if dia1 or dia2:
            return True
        return False

'''
Main Class with the main function named - game_is_on
'''
class Game(object):

    def __init__(self, board):
        self.current_player = "x"
        self.board = board
        self.current_player = "x"
        self.game_on = True
        self.validation = validation(self.board)

    def switch_player(self):
        if self.current_player == "x":
            self.current_player = "o"
        elif self.current_player == "o":
            self.current_player = "x"
        return

    def game_is_on(self):  #### Main Function
        self.board.display_board()
        while self.game_on == True:
            print(self.current_player, "'s turn")
            Flag1, Flag2 = False, False
            while Flag1 == False or Flag2 == False:
                position = input("Please enter a position 1-9 as per numpad layout and the position not taken- ")
                position = int(position) - 1
                Flag1, Flag2 = self.validation.validity_check(position)
            self.board.board[position] = self.current_player
            self.board.display_board()
            game_state = self.validation.check_if_game_over()
            if game_state == "winner":
                print("Winner is - ", self.current_player)
                return
            if game_state == "Tie":
                print("The Game is Tied")
                return
            self.switch_player()

def main():
    tic_tac_toe_board = Board()
    tic_tac_toe_game = Game(tic_tac_toe_board)
    tic_tac_toe_game.game_is_on()


main()
