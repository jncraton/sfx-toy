import os
import time
import random

from pyfiglet import Figlet
import getch
import pygame

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

colors = [RED, GREEN, BLUE, CYAN]

f = Figlet(font='doh', width=1602)

str = ''

pygame.init()
pygame.mixer.init()

sounds = {
  'b': 'bell',
  'c': 'cow',
  'd': 'dog',
  'f': 'fire',
  'h': 'horn',
  'p': 'plane',
  'r': 'rain',
  't': 'train',
  'w': 'whistle',
}

while True:
  char = getch.getch()

  os.system('clear')

  try:
    print(f.renderText(sounds[char]))

    pygame.mixer.music.load('sounds/' + sounds[char] + '.mp3')
    pygame.mixer.music.play()
  except KeyError:
    pass
