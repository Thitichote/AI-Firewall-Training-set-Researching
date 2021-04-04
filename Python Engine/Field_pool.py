
# Assign possible information each field

pool_action = {'allow': "1",
               'deny': "0"
               }

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

pool_ihl = {'20': '0101'} # 4 bits 5-16

pool_dscp = {'AF11':'001010', # 22
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