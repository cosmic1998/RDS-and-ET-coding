import numpy as np
import matplotlib.pyplot as plt

def get_orbit(initial_pt,a=0.1,alpha=3.1,iters=100):
    orbit_lst = [initial_pt]
    new_pt = initial_pt
    for i in range(iters):
        new_pt = new_pt-a*np.sin(2*np.pi*new_pt)+alpha
        new_pt = new_pt%1
        orbit_lst.append(new_pt)
    return np.array(orbit_lst)
