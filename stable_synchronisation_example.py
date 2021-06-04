from syncutils import *
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

a = 0.15 #Fix value of a
r = 0.6 #Fix value of r

k = 100 # Number of iterations

epsilon = 0.05

alphas = np.random.uniform(-1.0*r,1*r,size=k)
#Set initial points
x_0 = 0.3
x_1 = x_0 + epsilon

y_0 = 0.7
y_1 = 0.7 + epsilon

#Get orbit list
x_0_orbit_lst = fixed_noise_otbit(x_0, a, alphas)
x_1_orbit_lst = fixed_noise_otbit(x_1, a, alphas)

y_0_orbit_lst = fixed_noise_otbit(y_0, a, alphas)
y_1_orbit_lst = fixed_noise_otbit(y_1, a, alphas)


figure, axes = plt.subplots(1)
theta = np.linspace(0, 2*np.pi, 1000)
x_coord = np.cos(theta)
y_coord = np.sin(theta)
axes.set_title('Stable synchronisation of trajectories')

camera = Camera(figure)



for i in range(k):
    axes.set_aspect(1)
    if i < 10 or i%10 == 0:
        #Plot points and take a picture
        axes.plot(x_coord, y_coord,c='black')
        axes.scatter(np.cos(2*np.pi*x_0_orbit_lst[i]),np.sin(2*np.pi*x_0_orbit_lst[i]),c='red')
        axes.scatter(np.cos(2*np.pi*x_1_orbit_lst[i]),np.sin(2*np.pi*x_1_orbit_lst[i]),c='blue')

        axes.scatter(np.cos(2*np.pi*y_0_orbit_lst[i]),np.sin(2*np.pi*y_0_orbit_lst[i]),c='green')
        axes.scatter(np.cos(2*np.pi*y_1_orbit_lst[i]),np.sin(2*np.pi*y_1_orbit_lst[i]),c='purple')
        camera.snap()

#Save as gif
anim = camera.animate(blit=True)
anim.save('stable_sync_example.gif',writer='pillow')
