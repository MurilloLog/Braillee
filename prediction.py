# Identificador de codigo Braille
# Script para reconocer codigos generadores Braille utilizando OpenCV
# y TensorFlow
# 
# El script consiste en dibujar un codigo Braille dentro de un area de trabajo 
# predefinida. Mediante la posicion y los eventos del mouse se generan
# distintas formas que permitan el trazo o dibujado del caracter que se desea
# reconocer.
#
# Esta primera version solo permite trabajar con los codigos de las letras A 
# hasta la J. Para utilizarlo solo es necesario ejecutar el script, dibujar
# el codigo generador, guardar la imagen y llamar a la funcion de prediccion.
# Con los siguientes comandos sera posible la operacion del script:
#
#   'c'     :: Limpiar la pantalla
#   'p'     :: Salvar y predecir la imagen el sketch
#   'Esc'   :: Salir del programa
#
#   Operaciones con el mouse:
#   Clic primario : Dibujar un circulo con relleno
#   Clic secundario : Borrar un segmento del trazo actual
#   
#   Esta primer version solo permite dibujar circulos de un radio de 30 px en 
#   color negro sobre un fondo blanco. En futuras actualizaciones se considerara
#   agregar funcionalidades de diferentes trazos.
#

import cv2
import numpy as np
import csv
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

# Variables necesarias para el sketch
xInit, yInit = -1, -1   # Posicion inicial
length, width, dimension = 250, 250, 3
pencilSize = 30
pencilColor = (0,0,0)
sizeLine = 1
lineColor = (0,0,0)

# Variables necesarias para configurar la carga del modelo a utilizar
longitud, altura = 53, 53
modelo = './model/model.h5'
pesos_modelo = './model/pesos.h5'
cnn = load_model(modelo)    # Carga del modelo entrenado
cnn.load_weights(pesos_modelo)  # Carga de los pesos de la red

################## FUNCIONES PARA EL SKETCH ##################
# Funcion para generar el sketch
def createSketch(length, width, dimension):
    sketch = 255*np.ones((length, width, dimension), dtype=np.uint8)
    cv2.namedWindow('Sketchbook')
    return sketch

# Destruir el sketch al cerrar la aplicacion
def destroySketch():
    cv2.destroyAllWindows()
    
# Funcion para trazar la cuadricula del sketch
def sketchDiv(sketch, length, width, color, sizeLine):
    vLineInit = ((int)(width/2),0)
    vLineEnd = ((int)(width/2),length)
    cv2.line(sketch,vLineInit, vLineEnd, color, sizeLine)
    hLineInit_1 = (0,(int)(length/3))
    hLineEnd_1 = (width,(int)(length/3))
    cv2.line(sketch,hLineInit_1, hLineEnd_1, color, sizeLine)
    hLineInit_2 = (0,(int)(2*length/3))
    hLineEnd_2 = (width,(int)(2*length/3))
    cv2.line(sketch,hLineInit_2, hLineEnd_2, color, sizeLine)

# Funcion para limpiar el sketch
def cleanSketch(sketch):
    return 250*np.ones((length,width,3),np.uint8)

# Funcion para guardar el sketch como imagen jpg
def saveSketch(sketch):
    cv2.imwrite('./data/input/sketch.jpg', sketch)
    
# Función para dibujar sobre el lienzo
def sketchDraw(event, x, y, flags, param):    
    # Acciones a realizar en funcion de los eventos del mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(sketch,(x,y),pencilSize,(0,0,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(sketch,(x,y),30,(255,255,255),-1)
            
# Dibujando la cuadricula
def lines(sketch, initX, yInit, xEnd, yEnd, size):
    cv2.line(sketch, (initX, yInit), (xEnd, yEnd), size)
##############################################################
    
################ FUNCIONES PARA LA PREDICCION ################
def predict(file):
  global actual_prediction, row
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)   # Convertir la imagen en un arreglo
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)    # Array de dos dimensiones [[0,0...0]] donde la primer dimension contiene la cantidad de clases en el modelo
  # La prediccion arrojara como resultado un 1 en la clase correspondiente
  result = array[0] # La dimension 0 es la que incluye las clases del modelo entrenado
  answer = np.argmax(result)    # Obtiene el indice del elemento que tiene el valor mas alto
  # Proceso de comparacion entre cada indice del modelo entrenado
  print("\nLa CNN dice: ")
  with open("Training_indices.csv") as file:
      reader = csv.reader(file, delimiter=',')
      for row in reader:
          print("{}".format(row[answer]))
##############################################################

################ FUNCIONES PARA LA ESCRITURA ################
def add_char(strg):
    global text
    text += strg
##############################################################
          
    ##################### MAIN #####################
sketch = createSketch(length, width, dimension)
sketchDiv(sketch, length, width, lineColor, sizeLine)
cv2.setMouseCallback('Sketchbook', sketchDraw)

while True:
    cv2.imshow('Sketchbook', sketch)   
    interrupt = cv2.waitKey(1) & 0xFF
    if interrupt == ord('c'): # Limpiar el contenido de la imagen
        sketch = cleanSketch(sketch)
        sketchDiv(sketch, length, width, lineColor, sizeLine)
    elif interrupt == ord('p'): # Guardar y predecir imagen
        saveSketch(sketch)
        dir_image='./data/input/sketch.jpg'
        predict(dir_image)
    elif interrupt == 27:   # Cerrar aplicacion
        destroySketch()
        break

##############################################################

