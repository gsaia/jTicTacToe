from copy import deepcopy
import numpy as np


class InvalidPlayerError(Exception):
    pass

class InvalidMoveError(Exception):
    def __init__(self, message):
        print("INVALID MOVE!!")
        self.message = str(message)

class GameOver(Exception):
    def __init__(self, message):
        print("GAME OVER!!")
        self.message = message

class Game:
    BLANK = 'BLANK'

    def __init__(self, width = 3, height = 3, player1 = 'O'):
        self.__width__ = width
        self.__height__ = height
        self.__O__ = 'O'
        self.__X__ = 'X'
        self.board = self.init_board()
        self.players = [self.__O__,self.__X__ ]
        self.move_record = {self.__O__:[], self.__X__:[]}
        self.player1 = player1
        self.player2 = 'X'
        if self.player1 == self.__X__: self.player2 = self.__O__
        self.current_player = player1
        self.state = []
        
    def is_valid_move(self, x,y):
        # determines if move is a valid move
        # valid move means an available cell
        if self.board[x][y] == Game.BLANK : return True
        return False        
        
    def init_board(self):
        # creates and initializes the board with blank cells
        return[[Game.BLANK for i in range(self.__width__)] for j in range(self.__height__)]


    def is_goal_reached(self):
        #checks for the end of the game
        current_moves = self.move_record[self.current_player]
        #print (" Current moves of {0}: {1}".format(self.current_player,current_moves))
        if len(current_moves)<3: return False
        xs = 0
        ys = 0
        for i in range(len(current_moves)-1):
            for j in range(i+1, len(current_moves)):
                if current_moves[i][0] == current_moves[j][0]:xs += 1
                if current_moves[i][1] == current_moves[j][1]:ys += 1
        if(xs ==3 and ys ==0) or (ys == 3 and xs == 0) or (xs == 0 and ys == 0): return self.player_won(self.current_player)
        #print("Tallys: {0}, {1}".format(xs, ys))
        return False

    def get_valid_moves(self):
        #returns a list of (x,y) tuples which are the coordinates of BLANK cells
        moves = [(x,y) for x in range(self.__height__) for y in range(self.__width__) if self.board[x][y] == Game.BLANK]
        return moves
    
    def make_move(self,x,y):
        # it takes the coordinates of a cell and places the current player there.
        # then records the move and then switches the players
        result = False
        try:
            if not self.is_valid_move(x,y): raise InvalidMoveError((x,y)) 
                
            self.board[x][y] = self.current_player
            self.move_record[self.current_player].append((x,y))
            self.state.append(self.copy())
            
            if self.is_goal_reached():
                result = True
                GameOver((self.current_player + " WINS!!!"))  # handle the end of the game
        
        except InvalidMoveError as i:
            print(i.message, ' Not valid')

            
        except GameOver as g:
            print (g.message)
            result = True
            for state in self.state:
                print(state)
                
            #quit()
        else:
            self.switch_current_player()
        
        unique, counts = np.unique(self.board, return_counts=True)
        d = dict(zip(unique, counts))
        try:
            if not('BLANK' in d.keys()): raise GameOver('It is a tie :(')
        except GameOver as g:
            print (g.message , '\n')
            result = True
            for state in self.state:
                print(state)
                
            return result
        return result


    def switch_current_player(self):
        #switches the current player so the game can keep track of the next player's move
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
            
    def player_won(self, player):
        my_message = player + " WINS!!"
        raise GameOver(my_message)
        
    
    def copy(self):
        g = Game(width = self.__width__, height = self.__height__)
        g.board = deepcopy(self.board)
        g.player1 = self.player1
        g.player2 = self.player2
        g.current_player = self.current_player
        g.move_record[self.__O__]= self.move_record[self.__O__][:]
        g.move_record[self.__X__]= self.move_record[self.__X__][:]
        return g
    
    def __repr__(self):
        b = deepcopy(self.board)
        for i in range(len(b)):
            print("|", end = '')
            for j in range(len(b[i])):
                if b[i][j] == Game.BLANK: b[i][j] = '_'
                print(" {0} |".format(b[i][j]), end = '')
            print(' ')
        return " "
    
    def __str__(self):
        b = deepcopy(self.board)
        s = ''
        for i in range(len(b)):
            s += "| "
            for j in range(len(b[i])):
                if b[i][j] == Game.BLANK: b[i][j] = '_'
                s += str(b[i][j]) + " | "
            s += "\n"
        return s    