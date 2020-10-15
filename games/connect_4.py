
import numpy as np


class board():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid_size = (row,col)
        self.play_board = np.tile('_',self.grid_size)

    def display_board(self):
        print(self.play_board)
        print("\n")

    # Checks the availability of the spot and places the coin
    def update_board(self,player,column):  # pass the column-1 as the arguement
        if self.play_board[0][column] != '_':
            print("Sorry the column is full")
            return False, None
        else:
            for i in reversed(range(self.row)):
                if self.play_board[i][column] == '_':
                    self.play_board[i][column] = player
                    return True, i


'''
Chaecks for all the winning conditions
'''

class validation(object):
    def __init__(self,board):
        self.board = board

    def check_if_game_over(self, current_player, current_row, current_col):
        row_4 = self.row_win(current_player,current_row)
        col_4 = self.col_win(current_player,current_col)
        dia_bl_tr = self.dia_win_bl_tr(current_player,current_row,current_col)
        dia_tl_br = self.dia_win_tl_br(current_player,current_row,current_col)
        if row_4 == True or col_4 == True or dia_bl_tr == True or dia_tl_br == True:
            return True

    def row_win(self, current_player, current_row):
        count = 0
        for i in range(self.board.col):
            if self.board.play_board[current_row][i] == current_player:
                count += 1
                if count == 4:
                    return True
        return False

    def col_win(self, current_player, current_col):
        count = 0
        for i in range(self.board.row):
            if self.board.play_board[i][current_col] == current_player:
                count += 1
                if count == 4:
                    return True
        return False

    def dia_win_bl_tr(self, current_player, current_row, current_col):
        to_be_checked_row = [current_row+3,current_row+2,current_row+1,current_row,current_row-1,current_row-2,current_row-3]
        to_be_checked_col = [ current_col - 3,current_col - 2,current_col - 1, current_col, current_col + 1,
                             current_col + 2, current_col + 3]
        count = 0
        for i in range(len(to_be_checked_col)):
            if to_be_checked_row[i]>-1 and to_be_checked_row[i]<self.board.row and to_be_checked_col[i]>-1 and to_be_checked_col[i]<self.board.col:
                if self.board.play_board[to_be_checked_row[i]][to_be_checked_col[i]] == current_player:
                    count += 1
            if count == 4:
                return True
        return False

    def dia_win_tl_br(self, current_player, current_row, current_col):
        to_be_checked_row = [current_row+3,current_row+2,current_row+1,current_row,current_row-1,current_row-2,current_row-3]
        to_be_checked_col = [ current_col + 3, current_col + 2, current_col + 1,current_col, current_col - 1, current_col - 2, current_col - 3]
        count = 0
        for i in range(len(to_be_checked_col)):
            if to_be_checked_row[i]>-1 and to_be_checked_row[i]<self.board.row and to_be_checked_col[i]>-1 and to_be_checked_col[i]<self.board.col:
                if self.board.play_board[to_be_checked_row[i]][to_be_checked_col[i]] == current_player:
                    count += 1
            if count == 4:
                return True
        return False

    def check_if_tie(self, game_status):
        if game_status == True and '_' not in self.board.play_board:
            print("The game is a Tie")
            return True
        return False


class Game(object):
    def __init__(self, board):
        self.board = board
        self.validation = validation(board)
        self.current_player = "x"
        self.game_on = True

    def flip_player(self):
        if self.current_player == "x":
            self.current_player = "o"
        elif self.current_player == "o":
            self.current_player = "x"
        return

    def game_is_on(self):
        self.board.display_board()
        winner = False
        tie_status = False
        while self.game_on == True:
            print(self.current_player, "'s turn")
            current_row = 0
            column_availability_flag = False
            while column_availability_flag == False:
                player_column = input("Please enter the column number between %s and %s - "%(1,self.board.col))
                player_column = int(player_column)-1
                if player_column <= self.board.col and player_column >= 0:
                    column_availability_flag, current_row = self.board.update_board(self.current_player, player_column)
            self.board.display_board()
            winner = self.validation.check_if_game_over(self.current_player, current_row, player_column)
            if winner == True:
                print("Winner is- ",self.current_player)
                self.game_on = False
            if winner == False:
                tie_status = self.validation.check_if_tie(self.game_on)
                if tie_status == True:
                    self.game_on = False
            self.flip_player()



b = board(6,6)
g = Game(b)
g.game_is_on()
