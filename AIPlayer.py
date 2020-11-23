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

    def score(self, game, maximizing_player_turn=True):
        s = 0
        ''' 
        # TODO:  This is a utility function.  It should return a value according
                 to the goodness of a particular cell.
        # '''
        return s
    

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
    