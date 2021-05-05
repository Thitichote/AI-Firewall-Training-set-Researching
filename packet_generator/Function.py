from packet_generator import *
from packet_generator.rule_requirement import *
from packet_generator.rule_assign import *
from packet_generator.generate_field import *
import time



def generate_packet():

    requirement = read_csv()
    
    rule_list = assign_all_rule()
    
    for req in requirement: # each file
    
        begin = time.time()
        print(req[38])
        file_name = req[38] + '.csv'
        
        count = 0
        train_set_before = []
        
        for rule in rule_list: # each rule
            # number of each rule use => req[count]
            
            temp_src = assign_ip_pool(rule['SourceIP'])
            temp_dst = assign_ip_pool(rule['DestinationIP'])
            
            for i in range(int(req[count])): # each packet
                temp_packet = [
                    assign_Action(rule['Action']),
                    assign_Version(rule['Version']),
                    assign_IHL(rule['IHL']),
                    assign_DSCP(rule['DSCP']),
                    assign_ECN(rule['ECN']),
                    assign_InterfaceID(rule['InterfaceID']),
                    assign_Direction(rule['Direction']),
                    assign_IP(temp_src),
                    assign_Port(rule['SourcePort']),
                    assign_IP(temp_dst),
                    assign_Port(rule['DestinationPort']),
                    assign_Protocol(rule['Protocol'])
                ]
                train_set_before.append(temp_packet)
            count += 1
        
        # finish gen packet
        # -- convert data
        train_set_after = []
        binary = []
        for i in train_set_before:
            for j in i:
                for k in j:
                    binary.append(k)
            train_set_after.append(binary)
            binary = []
        
        with open(file_name, 'w', newline='') as myfile:
            print('making csv file... ', file_name)
    
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        
            wr.writerow(generate_field())
        
            for i in train_set_after:
                wr.writerow(i)
            
        shutil.move(file_name, "_csv/train_set/" + file_name)
        
        generate_time = time.time() - begin
        
        with open('_csv/result/generate_result.csv', 'a', newline='') as myfile:
            print('recording... ', file_name)
    
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        
            wr.writerow([file_name[:-4], len(train_set_before), generate_time])
            
            print(file_name[:-4]+ '.csv,', len(train_set_before), 'packets,', generate_time)
            
    print('done..')
    
    # debug1 = train_set_after
    
    # return debug1