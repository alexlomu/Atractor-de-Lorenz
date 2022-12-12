import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

'''

Este programa es un ejemplo de dos 
temas interesantes: el atractor de Lorenz 
y la resolución de un sistema de ecuaciones 
diferenciales ordinarias usando el modulo scipy.

'''

def lorenz(u,t):
    """
    Sistema de Lorenz
    """
    #s=10; r=28; b=2.667
    s=0.5; r=28; b=2.06
    ux_dot = s*(u[1] - u[0])
    uy_dot = r*u[0] - u[1] - u[0]*u[2]
    uz_dot = u[0]*u[1] - b*u[2]
    return [ux_dot, uy_dot, uz_dot]

#Condicion inicial
u0 = [0., 1., 1.05]

#Tiempo 
t = np.linspace(0,100,10000)

#Soluciones
u = odeint(lorenz,u0,t)

#Gráfica
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(u[:,0], u[:,1], u[:,2], lw=0.5)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Atractor de Lorenz")
plt.show()