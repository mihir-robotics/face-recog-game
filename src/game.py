# Pygame code
# REFACTORED

import pygame , random
from pygame.locals import *

#Initialising pygame stuff

pygame.init()
SIDE = 400
running = True

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SIDE,700),pygame.DOUBLEBUF)
pygame.display.set_caption('The Face Game')

# Store the score
score = 0

# Load the fonts

font_30 = pygame.font.SysFont("Arial", 25, True, False)
text_title = font_30.render("Face Gaem ", True, (255,255,255))

#Defining player class and related functions

#Defining some colors for convinience
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (159, 163, 168)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CAR_COLOR = (181, 230, 29)
TEXT_COLOR = (255, 255, 255)

class Sprite:

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
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(BLACK)

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    def draw_rect(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height], 0)

    def check_out_of_screen(self):
        if self.x+self.width > 400 or self.x < 0:
            self.x -= self.dx


def check_collision(player_x, player_y, player_width , player_height, car_x, car_y, car_width, car_height):
    if (player_x+player_width > car_x) and (player_x < car_x+car_width) and (player_y < car_y+car_height) and (player_y+player_height > car_y):
        return True
    else:
        return False

#Load the player sprite
player = Sprite(175,475,0,0,70,131,WHITE)
player.load_image("assets\MihirGameCringe1.png")
screen.set_alpha(None)
collision = True

#Load the falling objects (obs)
obs = []
obs_count = 1      #Can be changed to increase difficulty
for i in range(obs_count):
    x = random.randrange(0 , 340)
    ob = Sprite(x, random.randrange(-150, -50), 0, random.randint(5, 10), 30, 30,(0,255,0))
    obs.append(ob)

#Define the game over and main menu screen

def main_menu():
    screen.blit(text_title, [SIDE / 2 - 106, SIDE / 2 - 100])
    score_text = font_30.render(str(score), True, TEXT_COLOR)
    screen.blit(score_text, [SIDE / 2 - 70, SIDE / 2 - 30])
    
    pygame.display.update()

