# Generate Field

import random
import ipaddress

"""Action Field"""
# depend on rule
# allow or deny
# 1 bit
def assign_Action(var):
    if var == 'allow':
        return '1'
    elif var == 'deny':
        return '0'

"""Version"""
# alway Ipv4
# alway 0100
# 4 bits
def assign_Version(var):
    return "0100"

"""IHL"""
# alway any
# 5-16 = 11 possible
# 4 bits
def assign_IHL(var):
    return bin(random.randint(5,15))[2:].zfill(4)

"""DSCP"""
# alway any
# 22 possible
# 6 bits
def assign_DSCP(var):
    pool_dscp = {
        'AF11':'001010', # 22
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
    
    if var == 'any':
        return random.choice(list(pool_dscp.values()))
    else:
        return pool_dscp[var]

def assign_ECN(var):
# alway any
# 4 possible
# 2 bits
    return bin(random.randint(0,3))[2:].zfill(2)

def assign_InterfaceID(var):
# alway any
# 4 possible (eth0 - eth4)
# 4 bits
    return bin(random.randint(0,3))[2:].zfill(4)

def assign_Direction(var):
# alway any
# 2 possible (in, out)
# 1 bit
    return bin(random.randint(0,1))[2:].zfill(1)

def assign_Protocol(var):
# depend on rule
# 2 possible (tcp, udp)
# 8 bits
    pool_protocol = {
        'tcp': '00000110',
        'udp': '00010001'
        }
    if var == 'any':
        return random.choice(list(pool_protocol.values()))
    else:
        return pool_protocol[var]

def assign_Port(var):
# depend on rule
# 65536 possible
# 16 bits
    if var == 'any':
        return bin(random.randint(1,65535))[2:].zfill(16)
    else:
        return bin(int(var))[2:].zfill(16)

# ---------------------------

def assign_Src_ip(var):
    """a"""
# depend on rule
# 2^32 possible
# 32 bits
    

def assign_Dst_ip(var):
    """a"""
# depend on rule
# 2^32 possible
# 32 bits

def assign_ip_pool(var):
    pool_ip = []
    # should gen only 1st time
    if var[-3:] == '/32': # if subnet is 32
        pool_ip.append(var[:-3])
    elif var == 'any': # if address is any
        pool_ip.append('any')
    else:
        net4 = ipaddress.ip_network(var)
        for x in net4.hosts():
            pool_ip.append(str(x))
    return pool_ip

def assign_IP(pool_ip):
    # pool_ip = list of IP
    if pool_ip[0] == 'any':
        return str(bin(random.randint(1,4294967294))[2:].zfill(32))
    else:
        ip =  random.choice(pool_ip)
        list_octet = [bin(int(x)+256)[3:] for x in ip.split('.')]
        combine = list_octet[0] + list_octet[1] + list_octet[2] + list_octet[3]
        return combine

# data = 'any'
# test = assign_ip_pool(data)