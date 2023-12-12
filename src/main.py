''' 
Main()

#. Modules:
-   face (Local module)
-   game (Local module)

#. Function:
-   main():     Run the game & face functions.
'''

# Import the req. modules
import face
import game

# Main()
def main():
    # Set game state; if not True then stop/exit the game
    game.STATE = True
    while game.STATE:

        # Obtain face detection from video stream
        detections, h, w, frame = face.getFaceDetections(game.SIDE)

        # Get pygame event
        event = game.getEvent()
        # Quit game if pygame window is closed
        if event.type == game.pygame.QUIT:
            game.STATE = False

        # Start the game
        if game.collision and event.type == game.pygame.MOUSEBUTTONDOWN:
            game.collision = False
            # Init. the player stats
            game.player.x , game.player.dx, game.score = game.startGame(game.obs, game.obs_count, game.SIDE)
            
        if not game.collision:
            # Move player character
            game.player.x = game.SIDE - ((startX+10)*2)
        
        # Draw face rectangle, get co-ords of the box
        startX, startY, endX, endY = face.drawFace(detections, h, w, frame)

        # Drawing Code 
        game.screen.blit(game.background_img, (0,0))

        if not game.collision:
            # Start/ Draw player
            game.startPlayer(game.collision)

            # Draw the objects and update the score
            game.score = game.drawObj(game.obs, game.obs_count, game.score)
       
            # Checks collision for each object
            for i in range(game.obs_count):
                if game.check_collision(game.player.x, game.player.y, 30, 30, game.obs[i].x, game.obs[i].y, game.obs[i].width, game.obs[i].height):
                    game.collision = True
                    game.pygame.mouse.set_visible(True)
                    break
            
            # Draw the score
            game.drawScore(game.score)

        else:
            # Load main menu
            game.main_menu()
        
        # If 'q' is pressed, quit the game
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
