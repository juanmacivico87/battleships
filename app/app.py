from board.board import Board
from player.player import Player
from ship.ship import Ship

class App(object):
    def __init__(self):
        self.player = Player()
        self.board = Board()
        self.ship = Ship()
        
    def set_coordinate(self, axis):
        coordinate = self.board.board_length
                
        while(coordinate >= self.board.board_length):
            coordinate = input(f'Please, enter {axis} coordinate between 0 and {(self.board.board_length - 1)}: ')
            
            if (coordinate.isnumeric() == False):
                coordinate = self.board.board_length
                continue
                
            coordinate = int(coordinate)
        
        return coordinate
    
    def play(self):
        while(self.player.lifes > 0):
            x = self.set_coordinate('X')
            y = self.set_coordinate('Y')
            
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