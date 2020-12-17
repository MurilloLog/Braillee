# Braillee
## Algoritmo de reconocimiento Braille
En este repositorio se almacenan los archivos necesarios para montar una red neuronal convolucional (CNN) 
basada en Python destinada al reconocimiento de caracteres Braille.
Se podrá encontrar el dataset para entrenar a la CNN con diferentes ajustes así como los ultimos modelos
generados si solo se desea replicar el proyecto sin necesidad de realizar el entrenamiento.
## Comenzando
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local
para propósitos de desarrollo y pruebas.
### Requisitos
Antes de montar el proyecto localmente se debe asegurar que se cuentan con las siguientes librerias necesarias 
para funcionar.
- TensorFlow 2
- OpenCV
- Numpy
- CSV
- SYS

Si se tiene instalado el administrador de paquetes *pip* en cualquier version posterior a la 19, la instalación
de las librerias se puede realizar directamente como se muestra a continuación:
#### Instalación de [TensorFlow2](https://www.tensorflow.org/install)
```sh
pip install --upgrade pip
pip install tensorflow
```
#### Instalación de [OpenCV](https://opencv.org/)
```sh
pip install cv2
```
#### Instalación de [Numpy](https://numpy.org/install/)
```sh
pip install numpy
```
## Estructura del proyecto
La composición del proyecto esta constituida por dos scripts escritos en Python. Cada script es independiente uno
de otro y se ejecutan para diferentes propósitos:
- Script **training.py**: Para entrenar a la CNN bajo diferentes parámetros. Se necesita disponer de las imagenes
con las cuales se realizará el entrenamiento. Estas imagenes se encuentran clasificadas dentro del directorio
**./data/training/** y como resultado se genera el modelo de reconocimiento en el directorio **./model/** y el 
fichero **./Training_indices.csv** que almacena los indices de las clases de reconocimiento presentes en el modelo.
- Script **prediction.py**: Para ejecutar la aplicación de reconocimiento o probar la funcionalidad de la CNN. 
Se requiere la presencia de un modelo previamente entrenado y el fichero de los indices correspondientes a cada
clase del modelo. Por defecto carga el modelo presente en el directorio **./model/** y **./Training_indices.csv**.
### Composición de la imagen
Las imagenes de entrenamiento que se implementan para constituir el dataset tienen una dimensión de 53x53 px, la CNN
solo funciona con esta capacidad a excepción de ser modificada en su respectivo script de entrenamiento, puede
funcionar con magnitudes superiores ya que en ambos procesos automaticamente son redimensionadas con las desventajas 
que esto implica. No se recomienda utilizar imagenes inferiores a esta extensión debido a su perdida de resolución al ser
amplificadas.
La primera versión incluye 42 caracteres. Cada caracter tiene 100 muestras diferentes de las cuales 75 de ellas son 
dedicadas al proceso de entrenamiento y el resto al proceso de evaluación.
Las imagenes se encuentran debidamente reticuladas para enfatizar cada una de las regiones a introducir los signos 
generadores por lo que se espera sea mas sencillo aislar cada punto generador.

## Reconocimiento de imagen
Las imagenes presentes en el dataset, tanto las de entrenamiento como las de validación, son exclusivas para el proceso
de entrenamiento. Si se desea predecir una imagen externa al dataset es indispensable ejecutar el script **prediction.py**
mismo que proporcionará una ventana llamada "Sketchbook" con un lienzo de 250x250 px previamente cuadriculado donde será 
posible dibujar su propio signo generador.
Ejecutar este script se realiza de igual forma que cualquier otro script en Python:
```sh
python prediction.py
```

![sketchbook](https://user-images.githubusercontent.com/27164570/102543308-b6ad5c80-4078-11eb-955e-7e990548b3e9.JPG "Sketchbook")


## Sketchbook
Sketchbook funciona por medio de metacomandos y los eventos del mouse. Para manipular esta aplicación y obtener un resultado 
solo es necesario dibujar el código generador, guardar la imagen y llamar a la función de reconocimiento.
Con los siguientes comandos será posible manipular cada operación disponible:

**Operaciones con el teclado**
- 'c'   :: Limpiar la pantalla
- 'p'   :: Salvar y predecir la imagen el sketch
- 'Esc' :: Salir del programa

**Operaciones con el mouse**
- Clic primario   :: Dibujar un signo generador
- Clic secundario :: Borrar un segmento del signo generador

## Ejecución de pruebas
> Para la ejecución de pruebas se ha utilizado el IDE Spyder 3.3.6 con Python 3.7
### Reconocimiento acertado

![m_correcta](https://user-images.githubusercontent.com/27164570/102543415-e6f4fb00-4078-11eb-8624-93d20b409656.JPG "Correcto")

### Reconocimiento erroneo

![m_incorrecta](https://user-images.githubusercontent.com/27164570/102543468-f6744400-4078-11eb-94a0-56222d4ca189.JPG "Incorrecto")

### Tabla de resultados

![resultados](https://user-images.githubusercontent.com/27164570/102543897-99c55900-4079-11eb-9b18-55831c4d85be.jpg "Ponderación global")
