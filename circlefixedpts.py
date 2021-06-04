import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

#Fix number of points in the range to consider
num_pts = 50

#fix a
a = 0.1

alphas = np.linspace(0.01,a,num_pts)

#Create empty figure
fig = plt.figure()

#Create empty list
y_list = []
z_list = []
#Compute y_alpha and z_alpha
for i in range(num_pts):
    y_alpha =  np.arcsin(alphas[i]/a)/(2*np.pi)
    z_alpha =  0.5-y_alpha
    y_list.append(y_alpha)
    z_list.append(z_alpha)

#Plot graph of fixed points
plt.scatter(alphas,np.mod(y_list,1),c='black',alpha=1,label=r'$y_ \alpha$')
plt.scatter(alphas,np.mod(z_list,1),c='green',alpha=0.6,label=r'$z_ \alpha$')
plt.title(r"Plot of fixed points as $\alpha$ approaches $a$")
plt.xlabel(r"$\alpha$")
plt.ylabel("Fixed point")
plt.legend()
plt.show()
