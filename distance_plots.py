import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from syncutils import *

#Get orbit of chosen points
x_0 = get_orbit(0.3,0.1,0.08,150)
y_0 = get_orbit(0.8,0.1,0.08,150)


#Iterate the same homeomorphism and plot their ditsance
plt.plot(range(len(x_0)),np.abs(x_0-y_0))
plt.title("Distance between two points")
plt.xlabel("Iterations")
plt.ylabel("Distance")
plt.yscale("log")
plt.show()
plt.clf()

#Fix value of a
a = 0.1

#Fix random noise realisations
alphas = np.random.uniform(-2.0*a,2*a,100)
x_1 = fixed_noise_otbit(0.3,a,alphas)
y_1 = fixed_noise_otbit(0.8,a,alphas)
print(x_1.shape)

#Compute the distance between two different points x_1 and y_!
dists_two = np.abs(x_1-y_1)

#Plot distance
plt.plot(range(len(x_1)),dists_two)
plt.title("Distance between two points")
plt.xlabel("Iterations")
plt.ylabel("Distance")
plt.yscale("log")
plt.show()
