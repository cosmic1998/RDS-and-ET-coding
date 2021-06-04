from syncutils import *
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

a = 0.15 #Fix value of a
r = 0.6 #Fix value of r

k = 50 # Number of iterations

alphas = np.random.uniform(-1.0*r,r,size=k)
x_0 = 0.3 #Set initial points
x_1 = 0.7

#Get orbit points
x_0_orbit_lst = fixed_noise_otbit(x_0, a, alphas)
x_1_orbit_lst = fixed_noise_otbit(x_1,a,alphas)

figure, axes = plt.subplots(1)
theta = np.linspace(0, 2*np.pi, 1000)
x_coord = np.cos(theta)
y_coord = np.sin(theta)
axes.set_title('Synchronisation of two trajectories')

camera = Camera(figure)



for i in range(k):
    #Take the arc of the circle between f^n(x_0) and f^n(x_1)
    if x_0_orbit_lst[i] < x_1_orbit_lst[i]:
        arc = np.linspace(x_0_orbit_lst[i],x_1_orbit_lst[i])
    else:
        arc = np.linspace(x_1_orbit_lst[i],x_0_orbit_lst[i])
    axes.set_aspect(1)
    if i < 10 or i%10 == 0:
        axes.plot(x_coord, y_coord,c='black')
        #Plot the end points and the arc
        axes.scatter(np.cos(2*np.pi*x_0_orbit_lst[i]),np.sin(2*np.pi*x_0_orbit_lst[i]),c='red')
        axes.scatter(np.cos(2*np.pi*x_1_orbit_lst[i]),np.sin(2*np.pi*x_1_orbit_lst[i]),c='blue')
        axes.plot(np.cos(2*np.pi*arc),np.sin(2*np.pi*arc),c='orange')
        camera.snap()

anim = camera.animate(blit=True)
anim.save('third_case.gif',writer='pillow')
