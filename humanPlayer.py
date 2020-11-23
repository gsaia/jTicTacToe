from Game import Game
  
# class to allow a human player to play against the AIPlayer or randomPlayer
class humanPlayer:
    def __init__ (self):
        pass
        
    # returns a list of x,y tuples that are all the valid moves in the current state.
    def get_valid_moves(self, this_game):
            
        return this_game.get_valid_moves()
    
    
    def move(self, gm):
        '''
        # TODO: This method should show the human user the available valid moves 
                should allow the user to make a selection and then return the coordinates
                of the cell
        '''
        this_game = gm.copy()
        list_of_valid_moves = self.get_valid_moves(this_game)
        print('SELECT A LEGAL MOVE:')
        for i in range(len(list_of_valid_moves)):
            print (f'{i}:  {list_of_valid_moves[i]}')

        selection = False
        while not selection:
            m = input(f'Enter a number from 0 to {len(list_of_valid_moves)-1}:')
            if len(m)>1:
                selection = False
            elif m.isdigit():
                n = int(m)
                if n>= 0 and n<len(list_of_valid_moves):
                    selection = True
        x,y = list_of_valid_moves[int(n)]
        return x,y
    
    
    