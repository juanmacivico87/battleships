from os import system
from random import randint
from time import sleep

class Ship(object):
    max_ships = 5
    min_ships = 1
    num_ships = 0
    ships_found = 0
    ships = []
    
    def set_ships_coordinates(self, board):
        while(len(self.ships) < self.num_ships):
            x = randint(0, (board.board_length - 1))
            y = randint(0, (board.board_length - 1))
            
            if ([x, y] in self.ships):
                continue
            
            self.ships.append([x, y])

    def check_num_ships(self):
        if (self.num_ships.isnumeric() == False):
            system('clear')
            print('Sorry, this is not a number')
            return False

        self.num_ships = int(self.num_ships)

        if (self.num_ships > self.max_ships):
            system('clear')
            print('Sorry, but no more than %d ships are allowed on the board' % (self.max_ships))
            return False

        if (self.num_ships < self.min_ships):
            system('clear')
            print('Sorry, but to play you need at least %d ships on the board' % (self.min_ships))
            return False

        return True

    def set_num_ships(self):
        system('clear')
        self.num_ships = input('How many ships do you want on the board?? (Please, enter a number between %d and %d) \n' % (
            self.min_ships,
            self.max_ships
        ))

        is_valid_number = self.check_num_ships()

        while(is_valid_number == False):
            self.num_ships = input('How many ships do you want on the board?? (Please, enter a number between %d and %d) \n' % (
                self.min_ships,
                self.max_ships
            ))

            is_valid_number = self.check_num_ships()

        print('Great!!! %d ships coming up!!!' % (self.num_ships))
        sleep(2)