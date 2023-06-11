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
            print(f'Sorry, but no more than {self.max_ships} ships are allowed on the board')
            return False

        if (self.num_ships < self.min_ships):
            system('clear')
            print(f'Sorry, but to play you need at least {self.min_ships} ships on the board')
            return False

        return True

    def set_num_ships(self):
        system('clear')
        is_valid_number = False
        
        while(is_valid_number == False):
            self.num_ships = input(f'How many ships do you want on the board?? (Please, enter a number between {self.min_ships} and {self.max_ships}) \n')
            is_valid_number = self.check_num_ships()

        print(f'Great!!! {self.num_ships} ships coming up!!!')
        sleep(2)
        
    def find_ship(self, x, y):
        if ([x, y] not in self.ships):
            return False
        
        self.ships_found += 1
        self.ships.remove([x, y])
        return True