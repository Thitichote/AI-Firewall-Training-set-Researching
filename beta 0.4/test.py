# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:41:46 2020

@author: POP PC
"""

import ipaddress

net4 = ipaddress.ip_network('192.0.2.0/24')

str1 = str(net4.netmask)
print(str1)

ip = '192.168.1.1'

print('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]))