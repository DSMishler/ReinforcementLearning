# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:12:28 2019

@author: dsmis
"""

import numpy as np
import matplotlib.pyplot as plt

lattice_len = 10
lattice_height = 10
class Environment:
    def __init__(self):
        self.hidden_variable = False # cause Python
        self.agent_ID = np.zeros((lattice_len,lattice_height)) # represent where agents are located
        for i in range(0, self.agent_ID.shape[0]):
            for j in range(0, self.agent_ID.shape[1]):
                self.agent_ID[i][j] = 0
        return
    def plot_me(self):
        plt.figure()
        plt.contourf(np.transpose(self.agent_ID))
        plt.show()
        return