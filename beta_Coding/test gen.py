subnet_in_list = ['192.168.0.','192.168.1.','172.168.1.','10.0.0.']
bin_add = ['0','00','000','0000','00000','000000','0000000']
port_in_list = [21,23,25,80,143]
import random

def main():
    for i in range(int(input())):
        src_add = random_ip(1)
        dst_add = random_ip_dst(src_add)
        port = random_port()
        listt = [src_add, dst_add, str(port)]
        print(listt)
        print(data_pp_add(src_add), data_pp_add(dst_add))
        
def random_ip(meta):
    if meta == "any":
        return str(random.randint(1,254))+"."+str(random.randint(1,254))+"."+str(random.randint(1,254))+"."+str(random.randint(1,254))

    else:
        return random.choice(subnet_in_list) + str(random.randint(1,254))

def random_ip_dst(meta):
    temp = random.choice(subnet_in_list) + str(random.randint(1,254))
    if meta != temp:
        return random.choice(subnet_in_list) + str(random.randint(1,254))
    else:
        random_ip_dst(meta)

def random_port():
    return random.choice(port_in_list)

def data_pp_add(meta):
    meta += "."
    temp = ""
    ret = ""
    net_ip = ""
    for i in meta:
        if i != ".":
            temp += i
        elif i == ".":
            ret += str(bin(int(temp)))
            ret = ret.replace("0b","")
            while(True):
                if len(ret) != 8:
                    ret = "0" + ret
                else:
                    net_ip += ret
                    ret = ""
                    break
            temp = ""
    return net_ip
main()
