import sys
from combiners import tarkib
from consts import common_passwrods
from utils import intro, print_to_terminal, write_to_file

if '-h' in sys.argv[-1:0:-1]:
    intro()

dinamit = []
passw_list = []
input_passwords = []

a = input('add some clue : ')
b = a.split(' ')
for i in b:
    input_passwords.append(i)
print(f'got {a}, {input_passwords} added to clues ! ! !')
for i in input_passwords:
    passw_list.append(i)
    dinamit.append(i)

a = input('do you want to add most 20 common password to your passlist? (y/[N]])')
if a.lower() != 'n':
    for i in common_passwrods:
        passw_list.append(i)
a = input('do you want to add most 20 common password to your combine list? (y/[N]])')
if a.lower() != 'n':
    for i in common_passwrods:
        dinamit.append(i)

a = input('do you want to add all 8 digit numbers?(its consume about 8Gb ram) (y/[N]])')
if a.lower() == 'y':
    print('it can take a few minutes  ! ! !')
    for i in range(100000000):
        i = str(i)
        i2 = '0' * (len(i) - 8)
        passw_list.append(f'{i2}{i}'
                          )

a = input('do you want to add first 10M numbers to your pass combine list? (y/[N]])')
if a.lower() == 'y':
    for i in range(10000000):
        dinamit.append(str(i))

print(
    'select combine groups length, huge number create stronger passlist but consume more resources and take more time')
a = input('2~5 (default is 2)')

if int(a) > 1 and int(a) < 6:
    depths = int(a)
else:
    depths = 2

deraza = len(dinamit)
passw_list = tarkib(depths, deraza, passw_list, dinamit)

# outputs:

terminal_input = sys.argv[-1]

if '--no-grid' in sys.argv[-1:0:-1]:
    for i in passw_list:
        print(i)
elif '-w' in sys.argv[-1:0:-1]:
    write_to_file(passw_list=passw_list)

else:
    print_to_terminal(passw_list=passw_list)
