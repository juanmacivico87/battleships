from board.board import Board
from player.player import Player
from ship.ship import Ship

class App(object):
    def __init__(self):
        self.player = Player()
        self.board = Board()
        self.ship = Ship()
    
    def play(self):
        while(self.player.lifes > 0):
            x = input('Please, enter X coordinate (0 - 9)')
            
            if (x.isnumeric() == False):
                x = 0
                
            y = input('Please, enter Y coordinate (0 - 9)')
                
            if (y.isnumeric() == False):
                y = 0
                
            x = int(x)
            y = int(y)
            
            has_ship = self.ship.find_ship(x, y)
            self.board.display_box(x, y, has_ship)
            self.player.play(has_ship)
            self.board.print_board(self.player, self.ship)
            
            if (len(self.ship.ships) <= 0):
                print('\nYou\'re a winner!!!')
                return

        print('\nYou\'re a loser!!!')
        
    def run(self):
        self.player.set_player_name()
        self.ship.set_num_ships()
        self.ship.set_ships_coordinates(self.board)
        self.board.set_board()
        self.board.print_board(self.player, self.ship)
        self.play()
    
app = App()
app.run()