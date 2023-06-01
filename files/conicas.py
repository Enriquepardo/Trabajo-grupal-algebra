''' 
Este archivo contiene las funciones para graficar las cónicas.
'''

# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definimos la función para graficar las cónicas

def conicas(a,b,c,d,e,f):
    '''
    Esta función grafica las cónicas.
    '''
    # Definimos el dominio de las variables
    x = np.linspace(-10,10,100)
    y = np.linspace(-10,10,100)
    # Definimos la función de la cónica
    X,Y = np.meshgrid(x,y)
    F = a*X**2 + b*X*Y + c*Y**2 + d*X + e*Y + f
    # Graficamos la cónica
    plt.contour(X,Y,F,[0])
    plt.show()

