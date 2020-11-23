
import random    
from Game import Game, GameOver
  

class randomPlayer:
    def __init__ (self):
        pass
        
        
    def get_valid_moves(self, this_game ):  
        #print (f'Type of this_game: {type(this_game)}')
        list_of_valid_moves = this_game.get_valid_moves()
        if not list_of_valid_moves:
            raise GameOver("No valid moves left")
                    
        return list_of_valid_moves 
    
    def move(self, gm):
        this_game = gm.copy()
        list_of_valid_moves = self.get_valid_moves(this_game)
        m = random.choice(list_of_valid_moves)  
        x,y = m  
        return x,y
    
    