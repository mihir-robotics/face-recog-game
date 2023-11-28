# Main
# NEEDS TO BE REFACTORED

import face
import game

# Main()
def main():
    STATE = True
    while STATE:
        frame = face.vs.read()
        frame = face.imutils.resize(frame, width= game.SIDE, height = game.SIDE)
        # Convert frame to a blob
        (h, w) = frame.shape[:2]
        blob = face.cv2.dnn.blobFromImage(face.cv2.resize(frame, (300, 300)), 1.0, (300, 300), (103.93, 116.77, 123.68))

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
        
        for i in range(0,detections.shape[2]):

            confidence = detections[0 , 0 , i , 2]

            if confidence < 0.7:
                continue

            box = detections[0,0,i,3:7] * face.np.array([w,h,w,h])
            (startX,startY,endX,endY) = box.astype("int")

            text = "Face Window"
            y = startY - 10 if startY - 10 > 10 else startY + 10
            face.cv2.rectangle(frame, (startX, startY), (endX, endY),
                        (0, 0, 255), 2)
            face.cv2.putText(frame, text, (startX, y),
                        face.cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        
        face.cv2.imshow("Face", frame)


    #-------- LINE 167  --------#
    
    # Clean up
    cv2.destroyAllWindows()
    vs.stop()


if __name__ == "__main__":
    main()
