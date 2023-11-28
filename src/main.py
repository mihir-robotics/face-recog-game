# Main
# NEEDS TO BE REFACTORED

import face
import game
import cv2

STATE = True

# Main()
def main():
    while STATE:
        frame = face.vs.read()
        frame = imutils.resize(frame, width= game.SIDE, height = game.SIDE)
        # Convert frame to a blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (103.93, 116.77, 123.68))

        face.net.setInput(blob)
        detections = face.net.forward()

        event = game.pygame.event.poll()
        if event.type == game.pygame.QUIT:
            STATE = False

    if game.collision and event.type == game.pygame.MOUSEBUTTONDOWN:
        game.collision = False
        for i in range(game.obs_count):
            game.obs[i].y = random.randrange(-150,50)
            game.obs[i].x = random.randrange(0,350)
        game.player.x = 175
        game.player.dx = 0
        game.score = 0
        game.pygame.mouse.set_visible(False)

    if not game.collision:
        game.player.x = game.SIDE - ((startX+10)*2)
        
    #-------- LINE 147 --------#
    
        

if __name__ == "__main__":
    main()
