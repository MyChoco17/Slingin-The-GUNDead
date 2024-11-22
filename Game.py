from MainMenu import *
from GameLoop import *
from pygame import *

# This initialises pygame and its sound module
init()
mixer.pre_init(44100, -16, 2, 2048)
# This is my main game loop, where it will loop over each while loop through functions.
while True:
    Main_Menu()
    Game_Loop()
    Game_Over()

