# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:19:13 2019

@author: dsmis
"""

import matplotlib.pyplot as plt
from matplotlib.offsetbox import (AnnotationBbox, OffsetImage)
from matplotlib.cbook import get_sample_data
import numpy as np
import Environment

def plot_all(grid, ghost, pacman, filename):
    
    '''
    An attempt to make it work :/
    # get pacman!
    fig, ax = plt.subplots()
    
    pacIm = get_sample_data('PacmanImg.png',asfileobj=False)
    arr_image = plt.imread(pacIm, format='png')
    
    imagebox = OffsetImage(arr_image, zoom=0.3)
    imagebox.image.axes = ax
    
    pos = [pacman.pos_x, pacman.pos_y]
    box = AnnotationBbox(imagebox, pos, xybox=(120., -80.),
                         xcoords = 'data',
                         boxcoords = "offset points",
                         pad = .5,
                         arrowprops = dict(
                                 arrowstyle="->",
                                 connectionstyle="angle,angleA=0,angleB=90,rad=3")
                         )
    ax.add_artist(box)
    '''
    fig = plt.figure( figsize = (10,10))
    cs = plt.contourf(np.transpose(grid.agent_ID))
    plt.axis('image')
    for i in range(grid.pellet_ID.shape[0]):
        for j in range(grid.pellet_ID.shape[1]):
            if grid.pellet_ID[i,j] == 1:
                plt.plot(i,j,'wo')
    plt.plot(ghost.pos_x, ghost.pos_y, 'ro', markersize = 20)
    plt.plot(pacman.pos_x, pacman.pos_y, 'yo', markersize = 25)
    plt.xlim(-0.5, Environment.lattice_len-.5)
    plt.ylim(-0.5, Environment.lattice_height-.5)
    plt.savefig(filename)
    plt.show()
