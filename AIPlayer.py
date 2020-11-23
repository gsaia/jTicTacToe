import numpy as np
from Game import Game, GameOver

'''
Each one of us should create a separate Evaluation Function.  
This function is one of the most important algorithms of thisapp.
It helps the minimax decide which move is the best move.

'''

class EvaluationFunction1:
    def __init__(self):    
        pass
        
    def score(self, game, maximizing_player_turn = True):
        s = 0
        ''' 
        # TODO:  This is a utility function.  It should return a value according
                 to the goodness of a particular cell.
        # '''
        return s
    
class EvaluationFunctionGenaro:
    def __init__(self):
        pass

    def score(self, game, max_player = True):
        '''
        Returns the score of the current move.
        :param game:  instance of Board.  it should have as last move the move to be evaluated
        :param max_player:    True or False
        :return:  Float
        '''
        self.i, self.j = self.get_last_move()
        self.player_symbol = self.get_player_symbol()
        score = 0
        self.game = game
        score += self.get_horizontal_score()
        score += self.get_vertical_score()
        score += self.get_diagonal_score()

        if max_player: return score
        return -score

    def get_horizontal_score(self):
        print(self.player_symbol)
        s = 0
        goal = 0
        width = self.game.get_width()
        for y in range(0, width):
            cell = self.game.board[self.i][(self.j +y + width) % width]
            if cell==Game.BLANK or cell == self.player_symbol: s+=1
            if cell == self.player_symbol: goal += 1
            print("s = {0}: x = {1}, y = {2}, horizontal goal = {3}".format(s, self.i, (self.j +y + width) % width, goal ))
        goal = 10 if goal == 3 else 1
        s = s if s == 3 else 0
        print('***horizontal s= ', s)
        return s * goal

    def get_vertical_score(self):
        s = 0
        height = self.game.get_height()
        goal = 0
        for x in range(0, height):
            cell = self.game.board[(self.i+ x + height) % height] [self.j]
            if cell==Game.BLANK or cell == self.player_symbol: s+=1
            if cell == self.player_symbol: goal += 1
            print("s = {0}: x = {1}, y = {2}, vertical goal = {3}".format(s, (self.i+ x + height) % height, self.j, goal))

        goal = 10 if goal == 3 else 1
        s = s if s == 3 else 0
        print('***vertical  s= ', s)
        return s * goal

    def get_diagonal_score(self):
        s1 = 0
        s2 = 0
        width = self.game.get_width()
        height = width
        goal1 = 0
        goal2 = 0
        if (self.i == int(height / 2) and self.j == int(width / 2)):

            for t in range (width):
                cell = self.game.board[t][t]
                if cell == Game.BLANK or cell == self.player_symbol: s1 += 1
                if cell == self.player_symbol: goal1 += 1
                y = width-1

            for t in range(width):
                cell = self.game.board[t][y]
                if cell == Game.BLANK or cell == self.player_symbol: s2 += 1
                if cell == self.player_symbol: goal2 += 1
                y -= 1
            s1 = s1 if s1 == 3 else 0
            s2 = s2 if s2 == 3 else 0
            goal1 = 10 if goal1==3 else 1
            goal2 = 10 if goal2 == 3 else 1
            s1 = s1 * goal1
            s2 = s2 * goal2
            s = s1 + s2
            print(s1,s2, s)
            return s

        if (self.i == 0 and self.j == 0) or (self.i == height-1 and self.j == width-1):
            for t in range (width):
                cell = self.game.board[t][t]
                if cell == Game.BLANK or cell == self.player_symbol: s1 += 1
                if cell == self.player_symbol: goal1 += 1

            goal1 = 10 if goal1 == 3 else 1
            s1 = s1 if s1 == 3 else 0
            return s1 * goal1

        if (self.i == 0 and self.j == width-1) or (self.i == height-1 and self.j == 0):
            y = width-1
            for t in range(width):
                cell = self.game.board[t][y]
                if cell == Game.BLANK or cell == self.player_symbol: s1 += 1
                if cell == self.player_symbol: goal1 += 1
                y -= 1

            goal1 = 10 if goal1 == 3 else 1
            s1 = s1 if s1 == 3 else 0
            return s1 * goal1

        return 0

    def is_terminal(self, game):
        '''
        :param game: Game
        :return:
        '''
        #game = self.game
        i, j = self.get_last_move()
        player_symbol = self.get_player_symbol()
        goal = 0
        width = game.get_width()
        # checks if there is a goal state in a row
        for y in range(0, width):
            cell = game.board[i][(j +y + width) % width]
            if cell == player_symbol: goal += 1
        utility_row = 100 if goal == 3 else 0

        print('***horizontal goal= ', utility_row)

        #checks if there is a goal state in a column
        height = game.get_height()
        goal = 0
        for x in range(0, height):
            cell = game.board[(i+ x + height) % height] [j]
            if cell == player_symbol: goal += 1

        utility_column =  100 if goal == 3 else 0

        print('***vertical  goal= ', utility_column)

        # Check if there is a goal state in a diagonal.
        goal1 = 0
        goal2 = 0
        if (i == int(height / 2) and j == int(width / 2)):

            for t in range (width):
                cell = game.board[t][t]
                if cell == player_symbol: goal1 += 1
                y = width-1

            for t in range(width):
                cell = game.board[t][y]

                if cell == player_symbol: goal2 += 1
                y -= 1
        utility_d1 = 100 if goal1 ==3 else 0
        utility_d2 = 100 if goal2 == 3 else 0

        goal1 = 0
        goal2 = 0
        if (i == 0 and j == 0) or (i == height-1 and j == width-1):
            for t in range (width):
                cell = game.board[t][t]
                if cell == self.player_symbol: goal1 += 1

        utility_d3 = 100 if goal1 == 3 else 0

        if (i == 0 and j == width-1) or (i == height-1 and j == 0):
            y = width-1
            for t in range(width):
                cell = game.board[t][y]
                if cell == player_symbol: goal2 += 1
                y -= 1

        utility_d4 = 100 if goal1 == 3 else 0

        return max(utility_row, utility_column, utility_d1, utility_d2, utility_d3, utility_d4)

    def get_player_symbol(self):
        '''
        Returns the symbol of the player's whose move needs to be evaluated

        :return: string
        '''

        symbol = self.game.last_move['player']
        return symbol


    def get_last_move(self):
        last_move = self.game.last_move['move']
        return last_move



    

class IAPlayer:
    def __init__(self, search_depth = 5, eval_fn = EvaluationFunction1()):
        
        ''' 
        * search_depth = minimax is a Depth first method.  limiting the search depth will force 
        * the algorithm to search the whole breath of the three at depth = search_depth.
        
        * eval_fn:  passed as an argument to explore different evaluation functions.
        
        '''
        self.eval_fn = eval_fn
        self.search_depth = search_depth
        
        
    # returns a list of x,y tuples that are all the valid moves in the current state.
    def get_valid_moves(self, this_game):
            
        return this_game.get_valid_moves()
    
    
    def move(self, gm):
        '''
        # TODO: This method should return a move
        * call minimax from here
        '''
        this_game = gm.copy()
        x,y = 0,0 
        
        
        return x,y
    
    def utility(self, game):
        """
        # TODO: update as required
        """
        return self.eval_fn.score(game)
    
    
    
    def minimax (self, game, depth = 5, maximizing_player=True):
        """ 
        # TODO: Finish as required.  
        # minimax is a recurring algorithm  
        # it should return the best move at the search level and its value.
        """    
        
        best_move = 0,0
        best_val = -100
        
        return best_move, best_val
    