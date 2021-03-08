from Function import *

begin = time.time()

file_name = 'train_set.csv'

number_1 = 1000
rule_1 = ['allow',
          'ipv4',
          '20',
          'any',
          'any',
          'any',
          'any',
          '192.168.1.0/24',
          'any',
          '200.100.100.0/24',
          'any',
          'any']

number_2 = 1000
rule_2 = ['allow',
          'ipv4',
          '20',
          'any',
          'any',
          'any',
          'any',
          '192.168.1.0/24',
          'any',
          '200.100.100.0/24',
          'any',
          'any']

make_data(rule_1, number_1)
make_data(rule_2, number_2)

write_csv(train_set_all, file_name)

end = time.time()

print("\n-result of generate packets-")
print("save as", file_name, len(train_set_all), 'packet(s)')
print('(', "%.2f" % (end-begin), 'seconds'+ ' )')

