# Main
'''
This should only contain the local imports (face, game).
Everything in 'while STATE...' shouldbe converted into methods/routines in their own respective files.
'''

import face
import game
from game import random as random

# Main()
def main():
    game.STATE = True
    while game.STATE:    # too long.. convert this into just routine calls to imports instead of if, for etc.
        frame = face.vs.read()
        frame = face.imutils.resize(frame, width= game.SIDE, height = game.SIDE)
        # Convert frame to a blob
        (h, w) = frame.shape[:2]
        blob = face.cv2.dnn.blobFromImage(face.cv2.resize(frame, (300, 300)), 1.0, (300, 300), (103.93, 116.77, 123.68))

        face.net.setInput(blob)
        detections = face.net.forward()

        event = game.getEvent()
        if event.type == game.pygame.QUIT:
            STATE = False

        # Start the game
        if game.collision and event.type == game.pygame.MOUSEBUTTONDOWN:
            game.collision = False
            for i in range(game.obs_count):
                game.obs[i].y = game.random.randrange(-150,50)
                game.obs[i].x = game.random.randrange(0,350)
            game.player.x = 175
            game.player.dx = 0
            game.score = 0
            game.pygame.mouse.set_visible(False)

        if not game.collision:
            game.player.x = game.SIDE - ((startX+10)*2)
        
        for i in range(0,detections.shape[2]):

            confidence = detections[0 , 0 , i , 2]

            if confidence < 0.7:
                continue

            box = detections[0,0,i,3:7] * face.np.array([w,h,w,h])
            (startX,startY,endX,endY) = box.astype("int")

            text = "Face"
            y = startY - 10 if startY - 10 > 10 else startY + 10
            face.cv2.rectangle(frame, (startX, startY), (endX, endY),
                        (0, 0, 255), 2)
            face.cv2.putText(frame, text, (startX, y),
                        face.cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        
        face.cv2.imshow("", frame)

        # Drawing Code 
        game.screen.fill((0,0,0))
        if not game.collision:
            game.player.draw_image()
            game.player.move_x()
            game.player.check_out_of_screen()

            # Check if objects move out of screen
            for i in range(game.obs_count):
                game.obs[i].draw_image()
                game.obs[i].y += 25
                if game.obs[i].y > 500:
                    game.score += 1
                    game.obs[i].y = random.randrange(-150,-50)
                    game.obs[i].x = random.randrange(0, 340)
                    game.obs[i].dy = random.randint(4, 9)        

            #
            for i in range(game.obs_count):
                if game.check_collision(game.player.x, game.player.y, 30, 30, game.obs[i].x, game.obs[i].y, game.obs[i].width, game.obs[i].height):
                    game.collision = True
                    game.pygame.mouse.set_visible(True)
                    break
            
            # Draw the score
            game.drawScore(game.score)

        else:
            game.main_menu()
        
        key = face.cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            game.pygame.quit()
            break

        # Set framerate; default is 100
        game.setFrameRate()
    
    # Clean up
    face.cleanup()

if __name__ == "__main__":
    main()
