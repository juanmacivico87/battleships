import os
import time

class App(object):
  player = ''
  max_ships = 5
  min_ships = 1
  num_ships = 0
  ships_found = 0
  board_length = 10
  score = 0
  lifes = 10
  empty = 'X'
  ship = 'O'
  unknow = '#'
  board = []
  ships = []

  def set_player_name(self):
    os.system('clear')
    self.player = input('What is your name?? \n')

    while(self.player == ''):
      os.system('clear')
      self.player = input('I couldn\'t read your name clearly. Please, could you tell me again?? \n')

    os.system('clear')
    print('Welcome to the game %s!!!' % (self.player))
    time.sleep(2)

  def set_board(self):
    for row in range(0, self.board_length):
      self.board.append([self.unknow for column in range(0, self.board_length)])

  def print_board(self):
    os.system('clear')
    print('Player: %s' % (self.player))
    print('Score: %d' % (self.score))
    print('Lifes: %s\n' % ('*' * self.lifes))

    for row in self.board:
      print((' ').join(row))

  def play(self):
    while(self.lifes > 0):
      x = input('Please, enter X coordinate (0 - 9)')
      y = input('Please, enter Y coordinate (0 - 9)')

      self.lifes -= 1
      self.print_board()

    print('\nYou\'re a loser!!!')


app = App()

app.set_player_name()
app.set_board()
app.print_board()
app.play()