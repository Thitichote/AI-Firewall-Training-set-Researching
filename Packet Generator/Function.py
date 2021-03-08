
# Function running random

from Field_pool import *
import ipaddress
import random
import sys
import csv
import time

count_rule = 0
train_set_all = []

def assign_action(var):
    if var == 'allow':
        return '1'
    elif var == 'deny':
        return '0'
    
def assign_ip(var):
    net4 = ipaddress.ip_network(var)
    pool_src_ip = [] # ignore
    for x in net4.hosts():
        pool_src_ip.append(str(x))
        
    ip =  random.choice(pool_src_ip)
    
    list_octet = [bin(int(x)+256)[3:] for x in ip.split('.')]
    combine = list_octet[0] + list_octet[1] + list_octet[2] + list_octet[3]
    
    return combine

def assign_direction(var):
    if var == 'any':
        return random.choice(list(pool_direction.values()))
    else:
        return pool_direction[var]
    
def assign_interfaceID(var):
    if var == 'any':
        return random.choice(list(pool_interfaceID.values()))
    else:
        return pool_interfaceID[var]
    
def assign_src_port(var):
    if var == 'any':
        return random.choice(list(pool_src_port.values()))
    else:
        return pool_src_port[var]
    
def assign_dst_port(var):
    if var == 'any':
        return random.choice(list(pool_dst_port.values()))
    else:
        return pool_dst_port[var]
    
def assign_protocol(var):
    if var == 'any':
        return random.choice(list(pool_protocol.values()))
    else:
        return pool_protocol[var]
    
def assign_version(var):
    if var == 'any':
        return random.choice(list(pool_version.values()))
    else:
        return pool_version[var]

def assign_ihl(var):
    if var == 'any':
        return random.choice(pool_ihl)
    else:
        return pool_ihl[var]
    
def assign_dscp(var):
    if var == 'any':
        return random.choice(list(pool_dscp.values()))
    else:
        return pool_dscp[var]
    
def assign_ecn(var):
    if var == 'any':
        return random.choice(pool_ecn)
    else:
        return var

def test_rule(rule):
    for i in range(3):
        print('------------- packet number:', i+1)
        print("Action: " + assign_action(rule[0])) # fix
        print("Version: " + assign_version(rule[1])) # fix
        print("IHL: " + assign_ihl(rule[2])) # fix
        print("DSCP: " + assign_dscp(rule[3])) # not fix
        print("ECN: " + assign_ecn(rule[4])) # not fix
        print("InterfaceID: " + assign_interfaceID(rule[5])) # not fix
        print("Direction: " + assign_direction(rule[6])) # not fix
        print("Source IP: " + assign_ip(rule[7])) # depend
        print("Source port: " + assign_src_port(rule[8])) # # not fix
        print("dest IP: " + assign_ip(rule[9])) # depend
        print("dest port: " + assign_dst_port(rule[10])) # not fix
        print("protocol: " + assign_protocol(rule[11])) # not fix

def write_csv(train_set_all, file_name):
    with open(file_name, 'w', newline='') as myfile:
        print('making csv file')
        column = ['Action','Version','IHL','DSCP','ECN','Total Length','InterfaceID','Direction','TTL','Source IP','Source Port','Destination IP','Destination Port','Protocol']
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    
        wr.writerow(column)
    
        for i in train_set_all:
            wr.writerow(i)

def make_data(rule, number):
    global train_set_all
    print_rule(rule, number)
    for i in range(number):
        train_set_all.append([assign_action(rule[0]),
                             assign_version(rule[1]),
                             assign_ihl(rule[2]),
                             assign_dscp(rule[3]),
                             assign_ecn(rule[4]),
                             assign_interfaceID(rule[5]),
                             assign_direction(rule[6]),
                             assign_ip(rule[7]),
                             assign_src_port(rule[8]),
                             assign_ip(rule[9]),
                             assign_dst_port(rule[10]),
                             assign_protocol(rule[11])])
    print('rule', count_rule, 'done..\n')
    # print(train_set_all)
        
def print_rule(rule, number):
    global count_rule
    count_rule = count_rule + 1
    print("-> rule", count_rule, ',' + str(number), 'packets')
    print("1 Action: " + rule[0]) # fix
    print("2 Version: " + rule[1]) # fix
    print("3 IHL: " + rule[2]) # fix
    print("4 DSCP: " + rule[3]) # not fix
    print("5 ECN: " + rule[4]) # not fix
    print("6 InterfaceID: " + rule[5]) # not fix
    print("7 Direction: " + rule[6]) # not fix
    print("8 Source IP: " + rule[7]) # depend
    print("9 Source port: " + rule[8]) # # not fix
    print("10 dest IP: " + rule[9]) # depend
    print("11 dest port: " + rule[10]) # not fix
    print("12 protocol: " + rule[11]) # not fix
    return 0
    
# ----------------------------------------------------------------------