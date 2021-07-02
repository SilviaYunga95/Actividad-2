#Programe el método de eliminación gaussiana y 
# halle el valor de estas temperaturas. 
# Utilice como apoyo el ejercicio del literal anterior.

# importo las librerias necesarias
import numpy as np

T = np.array([[4., -1., -1.,  0.],
              [-1., 4.,  0., -1.],
              [-1., 0.,  4., -1.],
              [0., -1., -1., 4.]])
D = np.array([30.,60.,40.,70.])

T1=np.copy(T)
D1=np.copy(D)
n=len(D)
print('Los puntos a cacular la temperatura son:')
print(T)
print(D)
for k in range(0,n-1):
    for i in range(k+1,n):
        mult= T[i,k]/T[k,k]
        for j in range(k,n):
            T[i,j]-=mult*T[k,j]
        D[i] -=mult*D[k]
x=np.zeros(n)
x[n-1]=D[n-1]/T[n-1,n-1]
for i in range(n-2,-1,-1):
    suma_j=0
    for j in range(i+1,n):
        suma_j += T[i,j]*x[j]
        x[i]=(D[i]-suma_j)/T[i,i]

print("\n La distribucion de temperaturaen la placa es:")
print(np.linalg.solve(T,D))