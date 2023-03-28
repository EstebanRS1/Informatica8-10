import numpy as np
import matplotlib.pyplot as plt

x=np.radians(np.arange(720))#crea un arreglo de 720 valores de 0 a 360 grados
plt.figure()#crea una figura

#Primer gráfico
plt.subplot(2,1,1)#2 filas, 1 columna, 1 gráfico
plt.plot(x,np.sin(x),label='seno')#grafica seno

#Agregar segundo gráfico
plt.subplot(2,1,2)#2 filas, 1 columna, 2 gráfico
plt.plot(x,np.cos(x),label='coseno')#grafica coseno
plt.show()