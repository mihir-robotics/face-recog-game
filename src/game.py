'''
Script handles the Game code modules and functions
#. Modules:
-   Pygame
-   Random

#. Objects:
-   player  (Player Sprite Object)
-   ob      (Object Sprite)
-   screen  (Pygame Display Object)

#. Functions
-   check_collision():  Check if object collided with player
-   main_menu():        Load the game's main menu; effective restart
-   getEvent():         Get the pygame.event object
-   setFrameRate():     Set the game framerate, using clock.tick()
-   checkObj():         Check if objects go below threshold, change score acc.
-   drawObj():          Draw the meteor object
-   drawScore():        Draw the game score
-   startPlayer():      Init. the player sprite
-   startGame():        Init. the game
'''
# Import req. modules
import pygame
from pygame.locals import *

# For object creation randomness
import random

#Initialising pygame
pygame.init()

# Window Size
SIDE = 400

# Game Title
GAME_TITLE = 'Face Recognition Game'
# Game State
STATE = True

# PNG Assets for Player & Object
PLAYER_ASSET = ".\\assets\\player.png"
OBJECT_ASSET = ".\\assets\\object.png"
BACKGROUND   = ".\\assets\\background.png"

# Defining some colors for convinience
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define screen for game
screen = pygame.display.set_mode((SIDE,SIDE*2),pygame.DOUBLEBUF)
pygame.display.set_caption(GAME_TITLE)

# Load background image
background_img = pygame.image.load(BACKGROUND).convert()

# Store the score
score = 0

# Load the fonts, set title
font_30 = pygame.font.SysFont("Arial", 20, True, False)
text_title = font_30.render(GAME_TITLE, True, WHITE)

# Set alpha value for screen
screen.set_alpha(None)

# Set collision default value
collision = True

# Defining Sprite class and related functions
class Sprite:
    '''
    Class to define player and object properties.

    Attributes:
        x (int): Horizontal position of the sprite.
        y (int): Vertical position of the sprite.
        dx (int): Horizontal velocity of the sprite.
        dy (int): Vertical velocity of the sprite.
        width (int): Width of the sprite.
        height (int): Height of the sprite.
        color (tuple): Color of the sprite (RGB tuple).

    Methods:
        load_image(img): Loads an image for the sprite.
        draw_image(): Draws the sprite on the screen.
        move_x(): Moves the sprite horizontally.
        move_y(): Moves the sprite vertically.
        check_out_of_screen(): Checks if the sprite is out of the screen boundaries and adjusts its position accordingly.
    '''
    # Init. function
    def __init__(self, x=0, y=0, dx=4, dy=0, width=30, height=30, color=WHITE):
        self.image = ""
        self.x = x
        self.y = y
        self. dx = dx
        self.dy = dy
        self.width = width
        self.height = height
        self.color = color

    def load_image(self, img):
        '''
        Loads an image for the sprite.

        Args:
        img (str): File path of the image.
        '''
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(BLACK)

    def draw_image(self):
        '''
        Draw the sprite on the screen
        '''
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        '''
        Move the sprite horizontally
        '''
        self.x += self.dx

    def move_y(self):
        '''
        Move the sprite vertically
        '''
        self.y += self.dy

    def check_out_of_screen(self):
        '''
        Check if sprite is out of screen and adjust the position acc.
        '''
        if self.x+self.width > SIDE or self.x < 0:
            self.x -= self.dx

# Collision code is checking collision against upper left corner of player hitbox (FIX THIS)
def check_collision(player_x, player_y, player_width , player_height, car_x, car_y, car_width, car_height):
    '''
    Checks collision between player and object.

    Args:
        player_x (int): X-coordinate of the player.
        player_y (int): Y-coordinate of the player.
        player_width (int): Width of the player.
        player_height (int): Height of the player.
        car_x (int): X-coordinate of the object to be checked for collision.
        car_y (int): Y-coordinate of the object to be checked for collision.
        car_width (int): Width of the object to be checked for collision.
        car_height (int): Height of the object to be checked for collision.

    Returns:
        collisionState: True if collision occurs, False otherwise.
    '''
    collisionState = False
    if (player_x+player_width > car_x) and (player_x < car_x+car_width) and (player_y < car_y+car_height) and (player_y+player_height > car_y):
        collisionState = True
    return collisionState

#Load the player sprite
player = Sprite(175,450,0,0,70,131)
player.load_image(PLAYER_ASSET)

#Load the falling objects (obs)
obs = []
obs_count = 2   #Can be changed to increase difficulty
for i in range(obs_count):
    x = random.randrange(0 , 340)
    # Init. object randomly within X-axis
    ob = Sprite(x, random.randrange(-150, -50), 0, random.randint(5, 10), 30, 30)
    # Load object asset
    ob.load_image(OBJECT_ASSET)
    # Add to list of objects to be spawned
    obs.append(ob)

#Define the game over and main menu screen
def main_menu():
    '''
    Draw the main menu/ game over screen of the game
    '''
    screen.blit(text_title, [SIDE / 2 - 106, SIDE / 2 - 100])
    score_text = font_30.render(str(score), True, WHITE)
    screen.blit(score_text, [SIDE / 2 - 70, SIDE / 2 - 30])
    pygame.display.update()

# Get pygame event 
def getEvent():
    '''
    Get the current pygame event through pygame.poll()

    Returns:
    - event:    Pygame event object
    '''
    event = pygame.event.poll()
    return event

# Set frame-rate for the game
def setFrameRate(fps = 120):
    clock = pygame.time.Clock()
    clock.tick(fps)

# Check if objects move outside of the screen; if yes -> increase score +1
def checkObj(ob, score):
    if ob.y > 500:
        score += 1
        ob.y = random.randrange(-150, -50)
        ob.x = random.randrange(0, 340)
        ob.dy = random.randrange(4, 9)
    
    return score
    
# Draw the object
def drawObj(obs, obs_count, score):
    for i in range(obs_count):
        obs[i].draw_image()
        obs[i].y += 25

        score = checkObj(obs[i], score)
    
    return score

# Draw the score
def drawScore(score):
    SCORESTRING = "Score: " + str(score)
    txt_score = font_30.render(SCORESTRING, True, WHITE)
    screen.blit(txt_score, [15,15])
    pygame.display.update()

# Start the player sprite, if collsion is not True
def startPlayer(collision):
    if collision is False:
        player.draw_image()
        player.move_x()
        player.check_out_of_screen()

# Initialise Game
def startGame(obs, obs_count, side):
    
    for i in range(obs_count):
        obs[i].y = random.randrange(-150, 50)
        obs[i].x = random.randrange(0, 350)
    
    player_x = side//2 - 25
    player_dx = 0
    game_score = 0
    pygame.mouse.set_visible(False)
    
    return player_x, player_dx, game_score
