import cv2

rtsp = "rtsp://root:pass@192.168.0.91:554/axis-media/media.amp"
video = cv2.VideoCapture(0)

while True:
    ret , frame = video.read()
    #Aplicamos espejos a los frames
    frame = cv2.flip(frame, 1)

    cv2.imshow("Detect Object", frame)
    
    t = cv2.waitKey(1)
    if (t == 27):
        break

video.release()
cv2.destroyAllWindows()
