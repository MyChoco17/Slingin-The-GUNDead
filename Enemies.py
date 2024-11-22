from pygame import *
from TexturesAndSounds import *
from Variables import *
import random

init()
# This is my enemy class, where all the values stored will go to create each enemy
class Enemy(sprite.Sprite):
    # This init function assigns all the base values
    def __init__(self, image, health, BaseSpeed, PointsWorth, Spawn_Pos, x, y):
        sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.health = health
        self.speed = BaseSpeed
        self.points = PointsWorth
        self.spawnpoint = Spawn_Pos
        self.xPos = x
        self.ypos = y
    # This draw function I created is so that I can call on self.draw and it will blit the textures to the display
    def draw(self):
        Display.blit(self.image, self.rect)
    # The move function makes it so that if the x or y value is smaller than the player x/y value,
    # it will increase or decrease based on positioning, to track the players' movement.
    def move(self, player):
        if self.rect.center != player.rect.center:
            if self.rect.x < player.rect.x:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed
            if self.rect.y < player.rect.y:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed
    # This function picks a random spawn position for the enemies
    def spawn(self, Spawn_Point):
        Spawn_Point = random.randrange(1,5)
        if Spawn_Point == 1:
            self.rect.x = 400
            self.rect.y = 20
        if Spawn_Point == 2:
            self.rect.x = 20
            self.rect.y = 375
        if Spawn_Point == 3:
            self.rect.x = 780
            self.rect.y = 375
        if Spawn_Point == 4:
            self.rect.x = 400
            self.rect.y = 730
    # This function respawns the enemy by creating new instances of the class and picking randomly which one to add to the sprite group, then spawning it
    def respawn(self):
        Waveinfunc = 1 # This simulates the Wave variable
        Enemies_Alive = len(Enemies.sprites()) # This gets the number of enemies alive by counting the sprites on screen
        if Enemies_Alive == 0:
            Waveinfunc += 1 # This simulates a new wave for each time there are 0 enemies alive
            for i in range((Spawn_Per_Wave * Waveinfunc) * 2):
                # This below me creates new enemy types, and picks between a random number between 1 and 3 to add the enemy to the sprite group
                New_Enemy_Type_Zombie = Enemy(ZombieTexture, 3, 2, 100, self.spawnpoint, x= any, y= any) 
                New_Enemy_Type_Heavy = Enemy(HeavyTexture, 6, 1, 300, self.spawnpoint, x= any, y= any)
                New_Enemy_Type_Speedy = Enemy(SpeedyTexture, 2, 3, 200, self.spawnpoint, x= any, y= any)
                Random_Number = random.randrange(1,4)
                if Random_Number == 1:
                    Enemies.add(New_Enemy_Type_Zombie)
                if Random_Number == 2:
                    Enemies.add(New_Enemy_Type_Heavy)
                if Random_Number == 3:
                    Enemies.add(New_Enemy_Type_Speedy)
                # This makes it so that for each enemy in the enemies sprite group, it spawns them all at the same time for each wave start
                for enemy in Enemies:
                    enemy.spawn(self.spawnpoint)
    # This is my collision function, where it will detect collision between the enemy and player, lowering player health, or enemy and bullet, killing the enemy
    def collision(self, player, bullet_shoot, ):
        # The cooldown is in ticks, and there is 120 ticks in a second, so it is 3 seconds of cooldown before damaging the player again
        global Cooldown
        Cooldown += 1
        if sprite.collide_rect(self, player) and Cooldown > 360:
            player.health -= 1
            Cooldown = 0
            mixer.Sound.play(Damage)
        if sprite.spritecollide(self, bullet_shoot, dokill= True):
            self.health -= 1
            # This checks if the enemy health is 0, and if it is, it will kill the enemy, and the random number between 1 and 6 picks whether it will have a chance of
            # spawning a heart or not
            if self.health == 0:
                Mob_Drop = random.randrange(1,6) # This generates a random number, and if that number is hit, the enemy will drop an additional heart for the player
                if Mob_Drop == 4:
                    Hearts = Health(Health_Image_Shrunk, spawnpoint= self.rect.center)
                    Extra_Hearts.add(Hearts) # Extra_Hearts is a sprite group that adds hearts and draws them on screen simultaneously
                    for heart in Extra_Hearts:
                        heart.draw()
                player.score += self.points
                self.kill()
# These are the starting enemies in wave 1
RandomValue = random.randrange(1,4)
Enemy_Type_Zombie = Enemy(ZombieTexture, 3, 2, 100, Spawn_Pos= (340, 70), x= any, y= any)
Enemy_Type_Heavy = Enemy(HeavyTexture, 6, 1, 300, Spawn_Pos= (340, 70), x= any, y= any)
Enemy_Type_Speedy = Enemy(SpeedyTexture, 2, 3, 200, Spawn_Pos= (340, 70), x= any, y= any)
# This creates my enemy sprite group, where I can continuously add enemies to it and respawn them
Enemies = sprite.Group()
Enemies.add(Enemy_Type_Heavy, Enemy_Type_Speedy, Enemy_Type_Zombie)

# This is my extra health class, where each time I kill an enemy, there is a chance for them to drop a health point
class Health(sprite.Sprite):
    def __init__(self, draw, spawnpoint):
        sprite.Sprite.__init__(self)
        self.image = Health_Image_Shrunk
        self.rect = self.image.get_rect()
        self.rect.center = spawnpoint
    def draw(self): # This draws the heart on screen
        Display.blit(self.image, self.rect)
    def spawn(self, spawnpoint):
        spawnpoint = Enemies.rect.center # This spawns the heart on the enemy once killed, and the 1/6 chance has been met
        self.rect = spawnpoint
    def collision(self, player):
        if sprite.collide_rect(self, player): # This checks for collision between the player, and when it happens, it kills the sprite, and adds 1 health point to the player
            player.health += 1
            self.kill()

Extra_Hearts = sprite.Group() # This is my hearts sprite group
