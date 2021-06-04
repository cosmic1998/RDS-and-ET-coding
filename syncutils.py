import numpy as np


def get_orbit(initial_pt,a=0.1,alpha=3.1,iters=100):
    '''
    Gets the orbit of a given point fixing alpha and a of the function
    f(a,alpha,x) = x - a*sin(2pi*x)+alpha
    Inputs:
    initial_pt: A float of the initial point
    a: A float fixing the value of a
    alpha: A float fixing the value of alpha
    iters: An integer counting the number of times we want to iterate this map

    Returns:
    orbit_list: A list of floats each float coressponding to an iterate of the map
    '''
    orbit_lst = [initial_pt]
    new_pt = initial_pt
    for i in range(iters):
        new_pt = new_pt-a*np.sin(2*np.pi*new_pt)+alpha
        new_pt = new_pt%1
        orbit_lst.append(new_pt)
    return np.array(orbit_lst)

def fixed_noise_otbit(initial_pt,a=0.1,alpha=None):
    '''
    Gets the orbit of two points under some fixed vector of noise realisations alpha
    with the same function as the get_orbit function except alpha changes at each iterate
    Inputs:
    initial_pt: : A float of the initial point
    a: A float fixing the value of a
    alpha: A nx1 numpy array of noise realisations
    Returns:
    orbit_list: A list of floats each float coressponding to an iterate of the map
    '''
    orbit_lst = [initial_pt]
    new_pt = initial_pt
    iters = len(alpha)
    for i in range(iters):
        new_pt = new_pt-a*np.sin(2*np.pi*new_pt)+alpha[i]
        new_pt = new_pt%1
        orbit_lst.append(new_pt)
    return np.array(orbit_lst)
