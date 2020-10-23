# -*- coding: utf-8 -*-
"""

Phase - 1 Packet Generator (Allow Based only)

Created on Thu Oct 22 11:02:27 2020

@author: POP PC

"""

# add rule possible here based on deny all, Any is exception
# rulebased = deny any any any any
rule_1 = 'allow 192.168.1.0 203.222.201.0 25'
rule_2 = 'allow 192.168.1.0 203.222.201.0 21'
rule_3 = 'allow 172.160.2.0 192.168.1.0 23'
rule_4 = 'allow 203.222.201.0 172.160.2.0 53'

# packet we want to generate
packet_want = 40

# name of files saved
csv_file_text = "%s.csv" % "Data_Text"

csv_file_bin = "%s.csv" % "Data_Binary"

csv_file_bin_split = "%s.csv" % "Data_Binary_Split"

# ip of source address and destination address possible
ip_pool = ["192.168.1", "172.160.2", "203.222.201"]

# mask is exception
mask = '255.255.255.0'

# port pool based on well known port (10)
port_pool = ['21', '22' ,'23', '25', '53', '80']
# port_pool_notused = ['21', '22' , '23', '25', '53', '80', '110', '143', '161', '443']

# add on what protocol of packet's port
tcp_list = ['21', '22', '23', '25', '80']
udp_list = ['53', '110', '143', '161', '443']

# prepared data for CSV export
full_data = []
full_data_bin = []
full_data_bin_split = []

# important variable of function 'info_to_binary'
zero_front = ["","0","00","000","0000","00000","000000",
                "0000000","00000000","000000000","0000000000",
                "00000000000"]

import random # random packet
import time # count time
import csv # export data

# packet random generating

def packet_generator():
    """Main Function of this program"""

    print("Starting . . . . . . . .")

    time_begin = time.time()

    print("Rule 1:", firewall_filter(rule_1))
    print("Rule 2:", firewall_filter(rule_2)) # -- > show firewall rule here
    print("Rule 3:", firewall_filter(rule_3))
    print("Rule 3:", firewall_filter(rule_4))

    for n_packet in range(packet_want):
        """random packet from the pool"""
        #time.sleep(0.2) #beware error
        print(".................. G E N E R A T I N G ...................")

        # this is list of 1 packet without decision
        raw_data = generate_packet_in_list()

        print("Packet gen: ", raw_data) # show here

        print("-> ", packet_action(raw_data))

        # packet_action() will decide this packet should Allow or Deny
        raw_data.insert(0, packet_action(raw_data)) # decision at list[0]

        # 1 packet we can convert to csv
        packet_data = raw_data

        # print("pre data: ", packet_data) # show here

        # insert to big list of many packets
        full_data.append(packet_data)

        """ Finish process of creating 1 packet """

    """ Export to CSV """
    print("Exporting", csv_file_text ,". . . . . . .")
    writing_csv_plain() # this file is plain text
    print("Done!")

    print("Exporting", csv_file_bin ,". . . . . . .")
    writing_csv_binary() # this file is binary for utility
    print("Done!")
    
    print("Exporting", csv_file_bin_split ,". . . . . . .")
    writing_csv_binary_split() # this file is binary for utility
    print("Done!")

    time_finish = time.time()
    time_duration = time_finish - time_begin
    print("Time created:", time_duration, "Seconds")
    print("Time per packet:", time_duration/packet_want, "Seconds")

    #-------------------------------------------------------------------#

def generate_packet_in_list():
    """ return [192.168.1.x, 192.168.2.x, port, protocol --> raw_data """

    ip_random_src = random.choice(ip_pool) + "." + str(random.randint(1, 254))
    ip_random_dst = random.choice(ip_pool) + "." + str(random.randint(1, 254))
    port_random = random.choice(port_pool)

    if port_random in tcp_list:
        protocol = '6'
    else:
        protocol = '17'

    return [ip_random_src, ip_random_dst, port_random, protocol]

def packet_action(raw_data):
    """ This Function will have rule decide the packet """

    if decide_decision(raw_data, firewall_filter(rule_1)) == 'allow':
        return '1'
    elif decide_decision(raw_data, firewall_filter(rule_2)) == 'allow':
        return '1'
    elif decide_decision(raw_data, firewall_filter(rule_3)) == 'allow':
        return '1'
    elif decide_decision(raw_data, firewall_filter(rule_4)) == 'allow':
        return '1'

    return '0'

def writing_csv_plain():
    """ This Function write from full data text to CSV text """
    with open(csv_file_text, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

        for i in range(packet_want):
            wr.writerow(full_data[i]) # write

def writing_csv_binary():
    """ This Function write from full data text to CSV binary """

    convert_bin() # convert full_data to full_data_bin with binary

    with open(csv_file_bin, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

        for i in range(packet_want):
            wr.writerow(full_data_bin[i]) # write

def convert_bin():
    """ Main Function to convert full of packets to binary CSV """

    for i in range(packet_want):

        # create temp list for temporary storage value
        temp_bin = []

        """ Only Decision not exist in function so we do here """
        temp_bin.append(full_data[i][0])

        # add data to temp list
        temp_bin.append(ip_to_binary(full_data[i][1])) # src_add 8x4 bit
        temp_bin.append(ip_to_binary(full_data[i][2])) # dst_add 8x4 bit

        temp_bin.append(info_to_binary(full_data[i][3], 16)) # port 16 bit
        temp_bin.append(info_to_binary(full_data[i][4], 8)) # protocol 8 bit

        # create full data of 1 packet
        full_data_bin.append(temp_bin)

def writing_csv_binary_split():
    """ This Function write from full data text to csv binary split"""
    
    convert_bin_split() # convert full_data_bin to full_data_bin_split
    
    with open(csv_file_bin_split, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

        for i in range(packet_want):
            wr.writerow(full_data_bin_split[i]) # write
    
def convert_bin_split():
    """ Main Function to convert full of binary packet to binary csv split """
    
    for i in range(packet_want):
        
        # create temp list for temporary storage value
        temp_bin = []
        
        """ Only Decision not exist in function so we do here """
        temp_bin.append(full_data_bin[i][0])
        
        # split source address to 4 octet
        temp_bin.append(full_data_bin[i][1][0:8])
        temp_bin.append(full_data_bin[i][1][8:16])
        temp_bin.append(full_data_bin[i][1][16:24])
        temp_bin.append(full_data_bin[i][1][24:32])
        
        # split dest. address to 4 octet
        temp_bin.append(full_data_bin[i][2][0:8])
        temp_bin.append(full_data_bin[i][2][8:16])
        temp_bin.append(full_data_bin[i][2][16:24])
        temp_bin.append(full_data_bin[i][2][24:32])
        
        temp_bin.append(info_to_binary(full_data[i][3], 16)) # port 16 bit
        temp_bin.append(info_to_binary(full_data[i][4], 8)) # protocol 8 bit

        # create full data of 1 packet
        full_data_bin_split.append(temp_bin)

""" These Function below here is data preprocessing """

def firewall_filter(firewall_rule):
    """ This Function change firewall rule to what we can calculate in list """

    # do spilt text of command
    action, src, dst, port = firewall_rule.split(" ")

    src = src.replace('.0','')
    dst = dst.replace('.0','')

    # if it is any so we choose all
    if src == 'any':
        src = ip_pool
    else:
        src = [src]

    if dst == 'any':
        dst = ip_pool
    else:
        dst = [dst]

    if port == 'any':
        port = port_pool
    else:
        port = [port]

    # return in list so we can calculate and use this variable
    return [action, src, dst, port]

def decide_decision(raw_data, checker):
    """ This Function will reduce the number of line to use for filtering """

    # same subnet can allow?
    if subnet_only(raw_data[0]) == subnet_only(raw_data[1]):
        return checker[0]

    if subnet_only(raw_data[0]) in checker[1]:
        if subnet_only(raw_data[1]) in checker[2]:
            if  raw_data[2] in checker[3]:
                return checker[0]
    return 'deny'

def subnet_only(ip):
    """ This Function change from full ip to only subnet mask 24 without last 0 """
    """ Example 192.168.1.254(input) --> 192.168.1(output) """

    for i in range(4): # the last digit can't go beyond 3
        if ip[::-1][i] == '.': # count from the last
            return ip[0:-(i+1)]

def ip_to_binary(data):
    """ This Function can convert binary of IP and Mask specific """
    """ because IP is not INT but STR so we need to split --> . <-- """
    """ 192.168.1.254(input) --> binary 32 bits(output) """

    # need empty variable to process
    data += "."
    temp = ""
    ip_bin = ""

    # count when find . then convert ip to 8 bit of 4 groups (octets)
    for i in data: # add
        if i == ".":
            ip_bin += info_to_binary(temp, 8)
            temp = ""
        elif i.isdigit(): # count
            temp += i
    return ip_bin

def info_to_binary(data, max_bin):
    """This Function can convert all data to binary"""

    # data is based on integer so we convert to INT
    data = int(data)

    # check if data is Subnet or Boardcast Address
    if data < 255 and data > 0:

        # we do need to full fill of packet header size 8 16 32
        zero_add = max_bin - len(str(bin(data))[2:])

        # delete first 2 charactor '0b'
        info_binary = str(bin(data))[2:]

        binary = zero_front[zero_add] + info_binary

        return binary
    else:
        return "input data is not correct (it might be 0 or 255 or else)"

packet_generator()
