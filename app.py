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

  def check_num_ships(self):
    if (self.num_ships.isnumeric() == False):
      os.system('clear')
      print('Sorry %s, this is not a number' % (self.player))
      return False

    self.num_ships = int(self.num_ships)

    if (self.num_ships > self.max_ships):
      os.system('clear')
      print('Sorry, but no more than %d ships are allowed on the board' % (self.max_ships))
      return False

    if (self.num_ships < self.min_ships):
      os.system('clear')
      print('Sorry, but to play you need at least %d ships on the board' % (self.min_ships))
      return False

    return True

  def set_num_ships(self):
    os.system('clear')
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
    time.sleep(2)

  def set_board(self):
    for row in range(0, self.board_length):
      self.board.append([self.unknow for column in range(0, self.board_length)])

  def print_board(self):
    os.system('clear')
    print('Player: %s' % (self.player))
    print('Ships: %d' % (self.num_ships))
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
app.set_num_ships()
app.set_board()
app.print_board()
app.play()