from Function import *

begin = time.time()

file_name = 'train_set.csv'

number_1 = 1000
rule_1 = ['allow',
          'ipv4',
          '20',
          'AF11',
          'any',
          'any',
          'any',
          '192.168.0.0/16',
          'any',
          '200.100.100.0/24',
          'any',
          'any']

number_2 = 1000
rule_2 = ['deny',
          'ipv4',
          '20',
          'AF12',
          'any',
          'any',
          'any',
          '192.168.3.0/24',
          'any',
          '200.100.100.0/24',
          'any',
          'any']

number_3 = 1000
rule_3 = ['deny',
          'ipv4',
          '20',
          'AF13',
          'any',
          'any',
          'any',
          '192.168.2.0/24',
          'any',
          '200.100.100.0/24',
          'any',
          'any']

make_data(rule_1, number_1)
make_data(rule_2, number_2)
make_data(rule_3, number_3)

train_set = contain_train_set()

count_column()

make_csv(train_set, file_name)

end = time.time()

print("\n-result of generate packets-")
print("save as", file_name, len(train_set_all), 'packet(s)')
print('(', "%.4f" % (end-begin), 'seconds'+ ' )')

