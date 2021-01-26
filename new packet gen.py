import time
import csv
import ipaddress
import random

"""Assign pool possible"""

pool_direction = {'in':"0",
                  'out':"1"
                  }
pool_interfaceID = {'eth0': "00",
                    'eth1': "01",
                    'eth2': "10",
                    'eth3': "01",
                    }

pool_src_ip_default = '192.168.0.0/16'

pool_src_port = {'ftp':'0000000000010101',
                 'http':'0000000001010000'
                 }

pool_dst_ip_default = '168.160.0.0/16'

pool_dst_port= {'ftp':'0000000000010101',
                 'http':'0000000001010000'
                 }

pool_protocol = {'tcp': '00000110',
                 'udp': '00010001'
                 }

pool_version = {'ipv4' : '0100'} # 4 bits

pool_ihl = ['1111', '1111'] # 4 bits

pool_dscp = {'AF11':'001010',
             'AF12':'001100',
             'AF13':'001110',
             
             'AF21':'010010',
             'AF22':'010100',
             'AF23':'010110',
             
             'AF31':'011010',
             'AF32':'011100',
             'AF33':'011110',
             
             'AF41':'100010',
             'AF42':'100100',
             'AF43':'100110',
             
             'CS1':'001000',
             'CS2':'010000',
             'CS3':'011000',
             'CS4':'100000',
             'CS5':'101000',
             'CS6':'110000',
             'CS7':'111000',
             
             'EF':'101110',
             }
pool_ecn = ['00','01','10','11'] # 2 bits
pool_total_length = [] # 16 bits
pool_ttl = [] # 8 bits

# rule Index about
# Index 0 = Action

# Index 1 = Version
# index 2 = IHL
# index 3 = DSCP
# index 4 = ECN
# index 5 = Total Length
# index 6 = InterfaceID
# index 7 = Direction
# index 8 = Time to live (TTL)

# Index 9 = Source IP Address
# Index 10 = Source Port
# Index 11 = Destination IP Address
# Index 12 = Destination Port
# Index 13 = Protocol
# -------------------

# version ihl ecn total ttl

rule_1 = ['allow', 'ipv4', '1111', 'AF11', 'any', '60', 'eth0', 'in', 'xx', '192.168.0.0/16', 'any', '168.160.0.0/16', 'any', 'tcp']

def assign_src_ip(var):
    net4 = ipaddress.ip_network(var)
    pool_src_ip = [] # ignore
    for x in net4.hosts():
        pool_src_ip.append(str(x))
        
    ip =  random.choice(pool_src_ip)
    
    list_octet = [bin(int(x)+256)[3:] for x in ip.split('.')]
    combine = list_octet[0] + list_octet[1] + list_octet[2] + list_octet[3]
    
    return combine

def assign_dst_ip(var):
    net4 = ipaddress.ip_network(var)
    pool_dst_ip = [] # ignore
    for x in net4.hosts():
        pool_dst_ip.append(str(x))
        
    ip =  random.choice(pool_dst_ip)

    ip =  random.choice(pool_dst_ip)
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
        return var
    
def assign_dscp(var):
    if var == 'any':
        return random.choice(list(pool_dscp.values()))
    else:
        return pool_dscp[var]
    
def assign_ecn(var):
    if var == 'any':
        return random.choice(pool_ecn)
    else:
        return pool_ecn[var]
    
def assign_total_length(var):
    if var == 'any':
        return random.choice(pool_total_length)
    else:
        # return pool_total_length[var]
        return "xxxxxxxxx"
    
def assign_ttl(var):
    if var == 'any':
        return random.choice(pool_ttl)
    else:
        # return pool_ttl[var]
        return 'xxxxxxxxx'

# main function
number_gen = 10
print("gen 20 ,type y1 or y2")
for i in range(number_gen):
    print("---------- packet number: ", i)
    print("Action: " + rule_1[0])
    print("Version: " + assign_version(rule_1[1]))
    print("IHL: " + assign_ihl(rule_1[2]))
    print("DSCP: " + assign_dscp(rule_1[3]))
    print("ECN: " + assign_ecn(rule_1[4]))
    print("Total Length: " + assign_total_length(rule_1[5]))
    print("Interface: " + assign_interfaceID(rule_1[6]))
    print("Direction: " + assign_direction(rule_1[7]))
    print("Time to live: " + assign_ttl(rule_1[8]))
    print("Source IP: " + assign_src_ip(rule_1[9]))
    print("Source port: " + assign_src_port(rule_1[10]))
    print("dest IP: " + assign_src_ip(rule_1[11]))
    print("dest port: " + assign_dst_port(rule_1[12]))
    print("protocol: " + assign_protocol(rule_1[13]))