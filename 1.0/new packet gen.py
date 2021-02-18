import time
import csv
import ipaddress
import random

csv_file_bin = "%s.csv" % "train_set"

"""Assign pool possible"""

pool_direction = {'in':"0",
                  'out':"1"
                  }
pool_interfaceID = {'eth0': "0000",
                    'eth1': "0001",
                    'eth2': "0010",
                    'eth3': "0001",
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

pool_ihl = {'20': '0101'} # 4 bits

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

rule_1 = ['allow', 'ipv4', '20', 'AF11', 'any', 'xx', 'eth0', 'any', 'xx', '192.168.0.0/16', 'any', '168.160.0.0/16', 'any', 'tcp']

def assign_action(var):
    if var == 'allow':
        return '1'
    else:
        return '0'

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
        return pool_ihl[var]
        # return "-"
    
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
    
def assign_total_length(var): # Exclude
    if var == 'any':
        return random.choice(pool_total_length)
    else:
        # return pool_total_length[var]
        return '0000000000000000'
    
def assign_ttl(var):
    if var == 'any':
        return random.choice(pool_ttl)
    else:
        # return pool_ttl[var]
        return '00000000'

def test_text():
    print("1 Action: " + assign_action(rule_1[0]))
    print("2 Version: " + assign_version(rule_1[1]))
    print("3 IHL: " + assign_ihl(rule_1[2]))
    print("4 DSCP: " + assign_dscp(rule_1[3]))
    print("5 ECN: " + assign_ecn(rule_1[4]))
    print("6 Total Length: " + assign_total_length(rule_1[5]))
    print("7 InterfaceID: " + assign_interfaceID(rule_1[6]))
    print("8 Direction: " + assign_direction(rule_1[7]))
    print("9 Time to live: " + assign_ttl(rule_1[8]))
    print("10 Source IP: " + assign_src_ip(rule_1[9]))
    print("11 Source port: " + assign_src_port(rule_1[10]))
    print("12 dest IP: " + assign_src_ip(rule_1[11]))
    print("13 dest port: " + assign_dst_port(rule_1[12]))
    print("14 protocol: " + assign_protocol(rule_1[13]))
    return 0

# main function
begin = time.time()

train_set_all = []

#------------------------------------------------------------------------------
rule = rule_1 # important
number = 300 # number want of rule
for i in range(number):
    if i % 10 == 0:
        print('-',end='')
    train_set_all.append([assign_action(rule[0]), assign_version(rule[1]), assign_ihl(rule[2]), assign_dscp(rule[3]), assign_ecn(rule[4]), 
                assign_total_length(rule[5]), assign_interfaceID(rule[6]), assign_direction(rule[7]), assign_ttl(rule[8]), 
                assign_src_ip(rule[9]), assign_src_port(rule[10]), assign_src_ip(rule[11]), assign_dst_port(rule[12]), 
                assign_protocol(rule[13])])
print(rule_1 + ' finish')

#------------------------------------------------------------------------------

with open(csv_file_bin, 'w', newline='') as myfile:
    print('making csv file')
    column = []
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(column)
    
    for i in train_set_all:
        wr.writerow(i)

end = time.time()

print("\nresult of generate packets")
print("rule 1 = ", number, "packets")
print("Time used =", end-begin, "Seconds")