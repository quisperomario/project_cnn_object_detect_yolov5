import cv2
import os

#TODO: aqui tenemos que cambiar el nombre del objeto
objeto =  "escalera de seguridad"
contenido = os.listdir('C:/Users/ROMAR/Downloads/'+objeto)
output_images_path = "C:/Users/ROMAR/Downloads/"+objeto+"/"
count = 1

for images  in contenido:
    archivo = "C:/Users/ROMAR/Downloads/"+objeto+"/"+images
    nombre_nuevo = output_images_path + objeto + str(count) + "_" + images
    os.rename(archivo, nombre_nuevo)
    count += 1
    