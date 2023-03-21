import torch
import cv2
import numpy as np
import pandas

#Leermos el modelo
model = torch.hub.load('ultralytics/yolov5','custom',
                        path='C:/Users/ROMAR/Desktop/PROGRAMACION/Project Neural Network/Vision Artificial/Deteccion Objetos/detect_object_v1/object.pt')

#Realizamos VideoCapture
cap = cv2.VideoCapture(0)

#Empezamos
while True:
    #Realizar lectura de la videocaptura
    ret, frame = cap.read()

    #Realizamos deteccion
    detect = model(frame)

    info = detect.pandas().xyxy[0]
    print(info)

    #Mostrar FPS
    cv2.imshow('Detector de Objetos', np.squeeze(detect.render()))

    #Leer el teclado
    t = cv2.waitKey(5)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()