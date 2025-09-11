import cv2
import matplotlib.pyplot as plt
import numpy as np

PATH_IMG_1 = "Material_TPs/TP1/img1_tp.png"
PATH_IMG_2 = "Material_TPs/TP1/img2_tp.png"

# Lectura de imagenes con CV2 y flag para escala de grises
img_1 = cv2.imread(PATH_IMG_1, cv2.IMREAD_GRAYSCALE)
img_2 = cv2.imread(PATH_IMG_2, cv2.IMREAD_GRAYSCALE)

# Hist - Visualizar el histograma completo con los 255 valores posibles, 255 bins
hist_1, bins_1 = np.histogram(img_1.ravel(), 255)
hist_2, bins_2 = np.histogram(img_2.ravel(), 255)

# Viz
fig_1 = plt.figure(figsize=(12, 8))

ax1 = plt.subplot(221)
ax1.imshow(img_1, cmap='gray', vmin=0, vmax=255)
ax1.set_title("Imagen 1")

ax2 = plt.subplot(222)
ax2.imshow(img_2, cmap='gray', vmin=0, vmax=255)
ax2.set_title("Imagen 2")

ax3 = plt.subplot(223)
ax3.plot(hist_1)
ax3.set_title("Histograma Imagen 1")

ax4 = plt.subplot(224)
ax4.plot(hist_2)
ax4.set_title("Histograma Imagen 2")

plt.show()
plt.savefig("results/histogramas_tp1.png")
'''
Comentarios
Las imagenes claramente son diferentes. En la imagen 1 simplemente se tiene un degrade en escala de grises mientras que en la segunda se tiene una flor.
Esta gran diferencia a nivel informacion no se muestra reflejada en los histogramas, ya que presentan exactamente los mismos valores. Probablemente se haya generado
la imagen 1 a partir de la imagen 2. Respecto a la cantidad de bins, primero se comienza por 255 para cubrir todo el rango dinamico de las imagenes en escala de grises.

Este es un gran contrajemplo que demuestra que el histograma de una imagen podria no representar unibvocamente una imagen, es decir tomarse como caracteristica al histograma de imagenes 
para ser usado en un algortimo de clasificacion/deteccion es un aceptable pero con su debida verficacion, ya que podria ocurrir este tipo de caso, donde dos imagenes completamente
distintas tienen el mismo histograma o muy parecido.

'''
