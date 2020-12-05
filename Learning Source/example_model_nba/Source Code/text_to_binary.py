add_leftover = ["","0","00","000","0000","00000","000000","0000000"]

def checker():
    while(True):
        print("Insert input here: ",end="")
        data = input()
        if "." in data:
            print(ip_to_binary(data))
        else:
            print(info_to_binary(data, 8))

def ip_to_binary(data):
    """This Function can convert ip and mask specific"""
    """data is an IP or Mask with 4 Octet"""
    data += "."
    temp, ip_bin = "", ""
    for i in data:
        if i == ".":
            ip_bin += info_to_binary(temp, 8)
            temp = ""
        elif i.isdigit():
            temp += i
    return ip_bin

def info_to_binary(data, max_bin):
    """This Function can convert all data to binary"""
    """data is an info, max_bin is an maximum size of packet header"""
    data = int(data)
    if data < 255 and data > 0:
        binary = add_leftover[max_bin - len(str(bin(data))[2:])] + str(bin(data))[2:]
        print('check the data is: ' + str(data) + "\nthe binary is: " + str(binary))
        return binary
    else:
        print("input data is not collect (it might be 0 or 255 or else)")
        return 0
    
checker()
