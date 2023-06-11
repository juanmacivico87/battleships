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
        # print(f'Help: {ship.ships}')
        print(f'Player: {player.name}')
        print(f'Ships: {ship.num_ships} ({ship.ships_found})')
        print(f'Score: {player.score}')
        print(f'Lifes: {("*" * player.lifes)}\n')

        for row in self.board:
            print((' ').join(row))
            
        print('\n')
        
    def display_box(self, x, y, has_ship):
        self.board[x][y] = self.ship if has_ship == True else self.empty
            