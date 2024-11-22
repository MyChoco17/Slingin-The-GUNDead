from pygame import *
init()
# This is where i'll add all of my textures

# Menu Textures for all 3 menus in game, the main menu, the scoreboard menu, and the game over screen
icon = image.load('Textures\\Menu\\icon.png')
display.set_icon(icon)
Menu_Background = image.load('Textures\\Menu\\Menu Background.png')
Menu_Logo = image.load('Textures\\Menu\\Menu Logo.png')
Game_Over_Screen = image.load('Textures\\Menu\\Graveyard.png')
Game_Over_Text = image.load('Textures\\Menu\\Game Over.png')
ScoreBoard_Background = image.load('Textures\\Menu\\Wanted Poster.png')
Load_To_Scoreboard_Text = image.load('Textures\\Menu\\Press Space.png')
Load_To_Game_Text = image.load('Textures\\Menu\\Press Enter.png')
Thanks_For_Playing_Text = image.load('Textures\\Menu\\Thank You.png')
Load_To_Menu_Text = image.load('Textures\\Menu\\Press Escape.png')
Exit_Game_Text = image.load('Textures\\Menu\\Exit Game.png')

# Player textures
Sheriff_Player = image.load('Textures\\Player\\Sheriff Standing.png')
Sheriff_Bullet = image.load('Textures\\Player\\Bullet.png')

# Enemy textures
ZombieTexture = image.load('Textures\\Enemy\\Basic.png')
SpeedyTexture = image.load('Textures\\Enemy\\Fast.png')
HeavyTexture = image.load('Textures\\Enemy\\Tank.png')

# Game Textures and GUI
Background_SandTiles = image.load('Textures\\Game\\Sand Background.png')
Health_Image = image.load('Textures\\Game\\Heart Texture.png')
Health_Image_Shrunk = transform.scale(Health_Image, (21,21))


# This is where I'll add sound effects and music for the game

def Menu_Background_Music():
    mixer_music.load('Sound Effects\\Menu Background Music.mp3')
    mixer_music.play(-1)
def In_Game_Music():
    mixer_music.load('Sound EFfects\\In-Game Music.mp3')
    mixer_music.play(-1)
    mixer_music.set_volume(0.175)

GunshotSFX = mixer.Sound('Sound Effects\\Gunshot.wav')
GunshotSFX.set_volume(0.3)
Yeehaw1 = mixer.Sound('Sound Effects\\Yeehaw 1.wav')
Yeehaw2 = mixer.Sound('Sound Effects\\Yeehaw 2.wav')
Damage = mixer.Sound('Sound Effects\\Damage.wav')
WompWomp = mixer.Sound('Sound Effects\\Womp Womp.wav')