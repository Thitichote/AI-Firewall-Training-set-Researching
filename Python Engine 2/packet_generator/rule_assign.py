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
    
# -----

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
      "SourceIP": '10.60.11.3/32',
      "SourcePort": 'any',
      "DestinationIP": '161.246.38.0/24',
      "DestinationPort": 'any',
      "Protocol": 'any'
    }
    
    rule21 = {
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
                 rule21,default]
    
    return rule_list