from pygame import *
from TexturesAndSounds import *
from Variables import *
from Enemies import *


# This is my Player class, where I'll add the texture, movement and hitbox to my player
class Player:
    def __init__(self, Player_xPos, Player_yPos, Health, Score):
        self.image = Sheriff_Player
        self.rect = self.image.get_rect()
        self.rect.center = (Player_xPos,Player_yPos)
        self.health = Health
        self.score = Score
        if self.health == 0:
            self.health += 4
        # This gets the texture for my player, and places a rectangular hitbox to it which follows the players position
    def draw(self):
        Display.blit(self.image, self.rect)
        # This draws the image and the rectangle onto the screen when called
    def move(self):
        playerspeed = 4
        Button_Press = key.get_pressed()
        if Button_Press[K_w]:
            self.rect.y -= playerspeed
        if Button_Press[K_s]:
            self.rect.y += playerspeed
        if Button_Press[K_a]:
            self.rect.x -= playerspeed
        if Button_Press[K_d]:
            self.rect.x += playerspeed
        self.rect.clamp_ip(Display.get_rect())
        # This defines the movement, and disables leaving the designated map area using clamping
    def shoot(self, bullet_shoot):
        # This gets the mouse position
        mouse_x, mouse_y = mouse.get_pos()

        # This calculates the direction of the angle from the player to the mouse using pygame's math calc, Vector2
        direction = math.Vector2(mouse_x - self.rect.centerx, mouse_y - self.rect.centery).normalize()
        AngleOfDirection = direction.angle_to(mouse.get_pos())
        AngleOfDirectionINT = int(AngleOfDirection)
        # This creates an instance of a bullet and adds it to the bullets sprite group
        Sheriff_Bullet_Angle = transform.rotate(Sheriff_Bullet, AngleOfDirectionINT - 30)
        # Sheriff_Bullet_Angle rotates the bullet image by calculating the angle of the mouse to the player, and directing the bullet to the mouse
        bullet_shoot = Bullet(self.rect.centerx, self.rect.centery, direction, Sheriff_Bullet_Angle)
        bullets.add(bullet_shoot)

# This is my bullet class, adding a bullet for each left click input registered
class Bullet(sprite.Sprite):
    def __init__(self, xPos, yPos, direction, image):
        sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (xPos, yPos)
        self.speed = 5
        self.direction = direction
    def draw(self):
        # This displays the bullet on screen
        Display.blit(self.image, self.rect)
    def update(self):
        # continuously moves the bullet in the direction it was shot at
        self.rect.x += (self.direction.x * self.speed)
        self.rect.y += (self.direction.y * self.speed)

# This creates my player, and also the bullet sprite group to add bullets to it when created
player = Player(Display_Width // 2, Display_Height // 2, PlayerHealth, 0)
bullets = sprite.Group()

