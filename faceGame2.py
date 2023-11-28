#Rewritten Version of Face Game

from imutils.video import VideoStream
import imutils
import numpy as np
import argparse , time , cv2
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
player.load_image("MihirGameCringe1.png")
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


#Constructing the argparse (I looked this part up online)
ap = argparse.ArgumentParser()

ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")

args = vars(ap.parse_args())

# Loading the model (which I took from the internet)
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

#Initialise the Video Stream 
vs = VideoStream(src=0).start()
time.sleep(2)

# Main()
while running:
    frame = vs.read()
    frame = imutils.resize(frame,width = SIDE, height = SIDE)
    # grab the frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (103.93, 116.77, 123.68))

    # pass the blob through the network and obtain the detections and predictions
    net.setInput(blob)
    detections = net.forward()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    if collision and event.type == pygame.MOUSEBUTTONDOWN:
        collision = False
        for i in range(obs_count):
            obs[i].y = random.randrange(-150,50)
            obs[i].x = random.randrange(0,350)
        player.x = 175
        player.dx = 0
        score = 0
        pygame.mouse.set_visible(False)

    if not collision:
        player.x = SIDE - ((startX+10)*2)
    
    
    for i in range(0,detections.shape[2]):

        confidence = detections[0 , 0 , i , 2]

        if confidence < args["confidence"]:
            continue

        box = detections[0,0,i,3:7] * np.array([w,h,w,h])
        (startX,startY,endX,endY) = box.astype("int")

        text = "dis Face"
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
                      (0, 0, 255), 2)
        cv2.putText(frame, text, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                    
    
    cv2.imshow("face",frame)

    #      Drawing Code goes below
    screen.fill((0,0,0)) 
    if not collision:
        player.draw_image()
        player.move_x()
        player.check_out_of_screen()

        # Checking if the objects move out of screen
        # Check if the enemy cars move out of the screen.
        for i in range(obs_count):
            obs[i].draw_rect()
            obs[i].y += 25 
            if obs[i].y > 500:
                score += 1
                obs[i].y = random.randrange(-150, -50)
                obs[i].x = random.randrange(0, 340)
                obs[i].dy = random.randint(4, 9)


        for i in range(obs_count):
            if check_collision(player.x,player.y, 30 , 30, obs[i].x,obs[i].y, obs[i].width,obs[i].height):
                collision = True
                pygame.mouse.set_visible(True)
                break
        
        # Draw the Score 
        txt_score = font_30.render("Score: "+str(score), True, WHITE)
        screen.blit(txt_score, [15, 15])
        pygame.display.update()
    
    else:
        main_menu()
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    clock.tick(100)

# clean up
cv2.destroyAllWindows()
vs.stop()