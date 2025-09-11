# computer_vision
Este repositorio contiene los codigos y experimentos realizados para la materia de Visión por Computador de la Maestría en Ciencias de la Computación.
Esta dividio en dos archivos, uno para cada punto del trabajo practico.
Para ejecutar los codigos, es necesario tener instalado Python 3.8 o superior, y las librerias listadas en requirements.txt. 
recomiendo usar un entorno virtual para instalar las dependencias.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Luego, para ejecutar cada punto, simplemente correr el archivo correspondiente:
```
python tp1_1.py
python tp2_1.py
```

Con respecto a la pregunta si es conveniente usar histogramas como features para clasificar una imagen, la respuesta es se puede usar, pero hay que tener en cuenta que en un histograma se pierde toda la informacion espacial de la imagen, es decir, se podria tener dos imagenes con el mismo histograma pero con contenido completamente diferente. Como lo visto en la figura 1. 
![Comparación de histogramas](results/histogramas_tp1.png)
Yo no lo recomendaría para tareas de clasificación de imágenes, ya que hay otras técnicas que preservan mejor la información espacial como la operacion de convolución con filtros.
Estas pueden capturar características locales y patrones en la imagen, lo que es crucial para tareas de clasificación.
