# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:26:16 2020

@author: POP PC
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import time
import os

print("input =",end="")
var = int(input())

for i in range(var):
# evenly sampled time at 200ms intervals
    
    time.sleep(2)
    
    plt.plot([0, 1, 2.35, 3, 4], [0, 3, 5.7, 2, 11])

    plt.xlabel('Months')
    plt.ylabel('Books Read')
    
    plt.savefig('result_{}.png'.format(int(time.time())))
    
    plt.show()