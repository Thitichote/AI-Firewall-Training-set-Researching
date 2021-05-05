# assign all rule used

# rule_assign.py

def assign_all_rule():

    rule1 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.3.0/24',
      "SourcePort": '1119',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '1119',
      "Protocol": 'tcp'
    }
    
    rule2 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.3.0/24',
      "SourcePort": '2099',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '2099',
      "Protocol": 'tcp'
    }
    
    rule3 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.3.0/24',
      "SourcePort": '5222',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '5222',
      "Protocol": 'tcp'
    }
    
    rule4 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.3.0/24',
      "SourcePort": '5222',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '5223',
      "Protocol": 'tcp'
    }
    
    rule5 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.3.0/24',
      "SourcePort": '5223',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '5222',
      "Protocol": 'tcp'
    }
    
    rule6 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.3.0/24',
      "SourcePort": '5223',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '5223',
      "Protocol": 'tcp'
    }
    
    rule7 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.3.0/24',
      "SourcePort": '27015',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '27015',
      "Protocol": 'udp'
    }
    
    rule8 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.3.0/24',
      "SourcePort": 'any',
      "DestinationIP": '10.60.11.3/32',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }

# ---
    
    rule9 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.5.0/24',
      "SourcePort": '1119',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '1119',
      "Protocol": 'tcp'
    }
    
    rule10 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.5.0/24',
      "SourcePort": '2099',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '2099',
      "Protocol": 'tcp'
    }
    
    rule11 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.5.0/24',
      "SourcePort": '5222',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '5222',
      "Protocol": 'tcp'
    }
    
    rule12 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.5.0/24',
      "SourcePort": '5222',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '5223',
      "Protocol": 'tcp'
    }
    
    rule13 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.5.0/24',
      "SourcePort": '5223',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '5222',
      "Protocol": 'tcp'
    }
    
    rule14 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.5.0/24',
      "SourcePort": '5223',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": '5223',
      "Protocol": 'tcp'
    }
    
    rule15 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.5.0/24',
      "SourcePort": '27015',
      "DestinationIP": '10.60.11.3/32',
      "DestinationPort": '27015',
      "Protocol": 'udp'
    }

    rule16 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.20.5.0/24',
      "SourcePort": 'any',
      "DestinationIP": '10.60.11.3/32',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule17 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '161.246.38.0/24',
      "SourcePort": 'any',
      "DestinationIP": '10.20.5.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule18 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '161.246.38.0/24',
      "SourcePort": 'any',
      "DestinationIP": '10.20.3.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule19 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.60.11.3/32',
      "SourcePort": 'any',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule20 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.10.0.0/16',
      "SourcePort": 'any',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }

    # ---------------------------------------------------------------------- this is limit for rule set 2

    rule21 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '161.246.0.0/24',
      "SourcePort": 'any',
      "DestinationIP": '192.168.5.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule22 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '156.87.62.0/24',
      "SourcePort": 'any',
      "DestinationIP": '137.251.75.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule23 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '198.175.30.0/24',
      "SourcePort": 'any',
      "DestinationIP": '216.40.100.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule24 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '96.183.127.0/24',
      "SourcePort": 'any',
      "DestinationIP": '52.172.64.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule25 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '192.168.0.0/16',
      "SourcePort": '80',
      "DestinationIP": '161.246.38.11/24',
      "DestinationPort": '80',
      "Protocol": 'tcp'
    }
    
    rule26 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '192.168.0.0/16',
      "SourcePort": '80',
      "DestinationIP": '161.246.38.11/24',
      "DestinationPort": '80',
      "Protocol": 'udp'
    }
    
    rule27 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '192.168.0.0/16',
      "SourcePort": '22',
      "DestinationIP": '161.246.38.11/24',
      "DestinationPort": '22',
      "Protocol": 'tcp'
    }
    
    rule28 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '192.168.0.0/16',
      "SourcePort": '22',
      "DestinationIP": '161.246.38.11/24',
      "DestinationPort": '22',
      "Protocol": 'udp'
    }
    
    rule29 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '100.100.0.0/16',
      "SourcePort": '80',
      "DestinationIP": '161.246.38.11/24',
      "DestinationPort": '80',
      "Protocol": 'tcp'
    }
    
    rule30 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '100.100.0.0/16',
      "SourcePort": '80',
      "DestinationIP": '161.246.38.11/24',
      "DestinationPort": '80',
      "Protocol": 'udp'
    }
    
    rule31 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.168.0.0/16',
      "SourcePort": 'any',
      "DestinationIP": '171.102.248.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule32 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '10.168.0.0/16',
      "SourcePort": 'any',
      "DestinationIP": '171.102.249.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule33 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '171.102.248.0/24',
      "SourcePort": 'any',
      "DestinationIP": '171.102.249.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule34 = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '192.168.1.0/24',
      "SourcePort": '22',
      "DestinationIP": '171.102.248.0/24',
      "DestinationPort": '22',
      "Protocol": 'tcp'
    }
    
    rule35 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '192.168.0.0/16',
      "SourcePort": 'any',
      "DestinationIP": '171.102.249.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule36 = {
      "Action": "allow",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": '216.40.100.0/24',
      "SourcePort": '80',
      "DestinationIP": '171.102.248.0/24',
      "DestinationPort": '80',
      "Protocol": 'any'
    }  
    
    default = {
      "Action": "deny",
      "Version": "ipv4",
      "IHL": 'any',
      "DSCP": 'any',
      "ECN": 'any',
      "InterfaceID": 'any',
      "Direction": 'any',
      "SourceIP": 'any',
      "SourcePort": 'any',
      "DestinationIP": 'any',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }

    rule_list = [rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,
                 rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,
                 rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,
                 rule31,rule32,rule33,rule34,rule35,rule36,
                 default]
    
    return rule_list