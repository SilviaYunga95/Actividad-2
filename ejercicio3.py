#método de sustitución regresiva. Analice el número de operaciones del algoritmo para
#matrices de tamaño 3x3.

#Importo librerias necesarias
import numpy as np
#Ingreso los valores de la matriz
A = np.array([[1,4,-5],[1,4,-2],[2,1,-1]])
# Ingreso los valores del temino independiente
b=np.array([3,5,3])
n=np.size(b) # determina el numero de filas
x=np.zeros(n) #calculo de solucion
for i in range(n-1,-1,-1):
    sumj=0
    for j in range (i+1,n):
        sumj +=A[i,j]*x[j]
    x[i]=(b[i]-sumj)*1/A[i,i]
print(x)