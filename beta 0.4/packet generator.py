# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:41:42 2020

@author: POP PC
"""

"""Assign Variable here"""

# the value number must %2 (or mod 2) = 0
packet_want = 100

import ipaddress

## ------------------------------------ POOL --------------------------
"""Assign IP soruce Address here"""
ip_src_all = []
net4 = ipaddress.ip_network('192.168.0.0/16')

for x in net4.hosts():
    ip_src_all.append(str(x))

"""Assign IP Destination Address here"""
ip_dst_all = ['192.168.20.1']
    
"""Assign Port here"""
port_all = ['21','23','80']

"""Assign Protocol here"""
protocol_all = ['tcp','udp']

## ------------------------------------ RULES --------------------------
"""Assign Firewall Rule here"""
rule_1 = ['allow', '192.168.1.0/28','192.168.20.1', '21', 'tcp']

import random

def generate_raw_packet():
    
    raw_data_packet = []
    
    for i in range(packet_want):
        ip_src_random = random.choice(ip_src_all)
        ip_dst_random = random.choice(ip_dst_all)
        src_mask = str(net4.netmask)
        dst_mask = '255.255.255.0'
        port_random = random.choice(port_all)
        protocol_random = random.choice(protocol_all)
        raw_packet = [ip_src_random, src_mask, ip_dst_random, dst_mask, port_random, protocol_random]
        raw_data_packet.append(raw_packet)
    
    return raw_data_packet
    
def generate_rule_packet():
    
    raw_data_packet = []
    net4 = ipaddress.ip_network(rule_1[1])
    net4_mask = str(net4.netmask)
    
    for x in net4.hosts():
        raw_data_packet.append([rule_1[0], str(x), net4_mask, rule_1[2], rule_1[3], rule_1[4]])
        
    return raw_data_packet



i = generate_raw_packet()
j = generate_rule_packet()
         

