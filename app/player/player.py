from os import system
from time import sleep

class Player(object):
    name = ''
    score = 0
    lifes = 10
    
    def set_player_name(self):
        system('clear')
        self.name = input('What is your name?? \n')

        while(self.name == ''):
            system('clear')
            self.name = input('I couldn\'t read your name clearly. Please, could you tell me again?? \n')

        system('clear')
        print('Welcome to the game %s!!!' % (self.name))
        sleep(2)