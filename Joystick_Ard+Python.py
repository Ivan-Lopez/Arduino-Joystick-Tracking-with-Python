import serial, time
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import random

arduino = serial.Serial('COM3', 9600) #Creamos objeto serial llamado Arduino y establecemos los parámetros de la conexión

fig, ax = plt.subplots()
x, y = 0,0
sc =ax.scatter(x,y)
plt.xlim(0,1023)
plt.ylim(0,1023)

def animate(i):
	rawString = arduino.readline()
	rawString.decode("utf-8")
	x, y=rawString.split()
	sc.set_offsets(np.c_[y,x]) #Con esto actualizamos el punto

    #ax.scatter(x,y)
    						   #Si utilizs scatter otra vez se crea uno nuevo

ani = matplotlib.animation.FuncAnimation(fig, animate, 
                frames=1, interval=10, repeat=True) 
ax.grid(True)
plt.show()