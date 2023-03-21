import cv2
import torch
import numpy as np
import pandas

#Leemos el modelo

modelo = torch.hub.load("ultralytics/yolov5", "custom",
path = "la ruta del modelo")

# Realizamos la videoCaptura
cap = cv2.VideoCapture(0)

# Empezamos
while True:
    #Realizamos lectura de la videocaptura
    ret, frame = cap.read()

    #Realizamos las detecciones
    detect = modelo(frame)

    #Estraer la informacion de la detecciones
    info = detect.pandas().xyxy[0]
    print(info)

    #Mostramos FPS
    cv2.imshow("Deteccion de Objetos", np.squeeze(detect.render()))

    # Leer el teclado
    t = cv2.waitKey(5)
    if t == 27:
        break


cap.release()
cv2.destroyAllWindows()




