from pygame import *
import random

# This initialises pygame and its sound module
init()
mixer.pre_init(44100, -16, 2, 2048)

# Game variables go here
FPS_Clock = time.Clock()
FPS = 120
font_for_text = font.Font(None, 36)
black = (0, 0, 0)
Menu_Run = True
Game_Run = True
Game_Over_Run = True
SB_Menu = True
PlayerHealth = 4
Wave = 1
Enemy_Spawn_Rate = 5
Spawn_Per_Wave = Wave * Enemy_Spawn_Rate
Cooldown = 0
# Display variables go here
Display_Width = 800
Display_Height = 750
Display = display.set_mode((Display_Width,Display_Height))
display.set_caption('''Slingin' The GUNdead''')
