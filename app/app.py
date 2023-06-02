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
            y = input('Please, enter Y coordinate (0 - 9)')

            self.player.lifes -= 1
            self.board.print_board(self.player, self.ship)

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