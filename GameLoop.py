from pygame import *
from PlayerChar import *
from TexturesAndSounds import *
from Enemies import *
from Variables import *

def Game_Loop():
    
    In_Game_Music() # This calls the function to play music whilst the game is running
    global Game_Run, Wave, Spawn_Per_Wave, PlayerHealth
    while Game_Run == True:
        Display.blit(Background_SandTiles, (0,0))
        FPS_Delta = FPS_Clock.tick(FPS) / 1000
        FPS_Clock.tick(FPS) # This is my framerate in the game
        Enemies_Alive = len(Enemies.sprites())
        for events in event.get():
            if events.type == QUIT:
                Game_Run = False
                exit()
            elif events.type == MOUSEBUTTONDOWN and events.button == 1: # This event gets a signal when once left click is pressed, a bullet will fire
                player.shoot(bullet_shoot= Sheriff_Bullet)
                mixer.Sound.play(GunshotSFX)
        if Enemies_Alive == 0: # This picks between 2 silly sounds to play once the wave ends and respawns new enemies
            RandNumb = random.randrange(1,2)
            if RandNumb == 1:
                mixer.Sound.play(Yeehaw1)
            if RandNumb == 2:
                mixer.Sound.play(Yeehaw2)
            Wave += 1
            enemy.respawn()

        for enemy in Enemies: # For each enemy in the Enemies sprite group, this calls the draw, move and collision function from my Enemy class
            enemy.draw()
            enemy.move(player)
            enemy.collision(player, bullets, )
        #This calls on my Player class and its functions draw to blit onto screen and move to allow user input to move
        player.draw()
        player.move()
        # "bullets" is a sprite group, and for each bullet created, it adds it to the group and calls on the bullet class' draw and update function
        for bullet in bullets:
            bullet.draw()
            bullet.update()
        # Extra_Hearts is a sprite group, and for each heart object created, it'll spawn it and check for collision
        for heart in Extra_Hearts:
            heart.draw()
            heart.collision(player)

        if player.health == 0: # If the player dies, the game is over, and will ask for the player name in the IDLE window
            Game_Run = False
            mixer_music.stop()

        # This is my GUI that displays things onto the screen such as text and images
        player_health = font_for_text.render(f"{player.health}", True, black)
        score_text = font_for_text.render(f"Score: {player.score}", True, black)
        wave_text = font_for_text.render(f"Wave: {Wave}", True, black)
        Display.blit(score_text, (10, 10))
        Display.blit(player_health, (650, 10))
        Display.blit(wave_text, (350, 10))
        Display.blit(Health_Image, (620,10))

        display.update()
