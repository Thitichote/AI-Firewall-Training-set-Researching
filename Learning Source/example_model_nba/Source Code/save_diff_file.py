# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:29:49 2020

@author: POP PC
"""

import time
    if os.path.exists('result.png'):
        plt.savefig('result_{}.png'.format(int(time.time())))
    else:
        plt.savefig('result.png')