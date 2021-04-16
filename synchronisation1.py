import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from syncutils import *


#Create circle skeleton
figure, axes = plt.subplots(1)
theta = np.linspace(0, 2*np.pi, 1000)
x_coord = np.cos(theta)
y_coord = np.sin(theta)
axes.set_title('Synchronisation of two trajectories')


#create camera to capture
camera = Camera(figure)


#Get orbit of points
x_0 = get_orbit(0.3,0.1,0.08,150)
y_0 = get_orbit(0.5,0.1,0.08,150)

#Animate points
for i in range(len(x_0)):
    axes.plot(x_coord, y_coord,c='black')
    axes.set_aspect(1)
    axes.scatter(np.cos(2*np.pi*x_0[i]),np.sin(2*np.pi*x_0[i]),c='red')
    axes.scatter(np.cos(2*np.pi*y_0[i]),np.sin(2*np.pi*y_0[i]),c='blue')
    camera.snap()

#Save as gif
anim = camera.animate(blit=True)
anim.save('sync.gif',writer='pillow')
