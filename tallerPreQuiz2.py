import numpy as np
import pandas as pd
import scipy.io as sio
import matplotlib.pyplot as plt

#1.Crear una matriz de Numpy aleatoria de 3 dimensiones y un size de 11520000
a=np.random.rand(288,160,250)#Filas,Columnas,Profundidad
#filas=288, columnas=160, profundidad=250

#2.Crea una copia de la matriz creada en el ítem anterior
b = a.copy()

#3.Muestra todos los atributos propios de dicha matriz , dimensión, tamaño, etc..
print(f"Forma: {a.shape}")
print(f"Tamaño: {a.size}")
print(f"Numero de Dimensiones: {a.ndim}")

#4.Modificar su forma y pasarla a 2D
a = a.reshape(288,160*250)#filas, columnas*profundidad
#filas=288, columnas=160*250
print(a)
print("\nMatriz 2D: ")
print(f"Forma: {a.shape}")
print(f"Tamaño: {a.size}")
print(f"Numero de Dimensiones: {a.ndim}")

#5.Crea una función que reciba la matriz anterior y la pase a un objeto tipo dataframe de Pandas
def aDataFrame(a):
    return pd.DataFrame(a)
# print(aDataFrame(a))
frame=aDataFrame(a)


#6.Crear una función que permita cargar un archivo .mat y .csv
def cargarArchivo(archivo):
    if archivo.endswith(".mat"):
        return sio.loadmat(archivo)
    elif archivo.endswith(".csv"):
        return pd.read_csv(archivo)
    
#7.Crear funciones de suma, resta, multiplicación, división, promedio, desviación estándar
#NOTA: Estas funciones deben permitir hacer estos procesos a lo largo de un eje (usando Numpy) ¿Cómo se implementaría usando Pandas?
def suma(a,axis=0):
    return np.sum(a,axis=axis)

def resta(a,axis=0):
    return np.diff(a,axis=axis)

def multiplicacion(a,axis=0):
    return np.prod(a,axis=axis)

def division(a,axis=0):
    return np.divide(a[:-1], a[1:], axis=axis)

def promedio(a,axis=0):
    return np.mean(a,axis=axis)

def desviacionEstandar(a,axis=0):
    return np.std(a,axis=axis)


#8.Crear una función que permita graficar un histograma de los datos de la matriz anterior
def graficarHistograma(a):
    plt.hist(a)
    plt.show()

#9.Crear una función que permita graficar un gráfico de barras de los datos de la matriz anterior
def graficarBarras(a):
    plt.bar(a, a)
    plt.show()

#10.Crear una función que permita graficar un gráfico de dispersión de los datos de la matriz anterior
def graficarDispersión(a):
    plt.scatter(a, a)
    plt.show()

#11.Crear una función que permita graficar un gráfico de stem de los datos de la matriz anterior
def graficarStem(a):
    plt.stem(a)
    plt.show()

#12.Crear una función que permita graficar un gráfico de pies de los datos de la matriz anterior
def graficarPie(a):
    plt.pie(a)
    plt.show()
print('Hello')
#ver las graficas
# graficarHistograma(a)
# graficarBarras(a)
# graficarDispersión(a)
# graficarStem(a)
# graficarPie(a)