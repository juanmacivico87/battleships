from os import system

class Board(object):
    board = []
    board_length = 10
    empty = 'X'
    ship = 'O'
    unknow = '#'
    
    def set_board(self):
        for row in range(0, self.board_length):
            self.board.append([self.unknow for column in range(0, self.board_length)])

    def print_board(self, player, ship):
        system('clear')
        # print('Help: %s' % (ship.ships))
        print('Player: %s' % (player.name))
        print('Ships: %d (%d)' % (ship.num_ships, ship.ships_found))
        print('Score: %d' % (player.score))
        print('Lifes: %s\n' % ('*' * player.lifes))

        for row in self.board:
            print((' ').join(row))
            
        print('\n')
        
    def display_box(self, x, y, has_ship):
        self.board[x][y] = self.ship if has_ship == True else self.empty
            