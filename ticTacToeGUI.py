#TODO: IMPORTS AS REQUIRED

#Class to graphically display the Tic Tac Toe board
class tttGUI:
    def __init__(self, game):
        self.init_GUI()
        self.game = game
        self.board = game.board
        self.init_GUI()
        self.display()
        
    
    def update(self, game):
        self.board = game.board 
        self.display()
        
    
    def display(self):
        """
        #TODO: Display the board.
        """
        pass
        
        
        