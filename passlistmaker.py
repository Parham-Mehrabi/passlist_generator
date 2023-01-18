import sys
import os
from time import sleep

if '-h' in sys.argv[-1:0:-1]:
    print('tags:'
          '\n\r help,h,H,h*              show this help'
          '\n\r --no-grid                make output in one line')
    print()
    intro = """if you would like to save the pass to a file
    i suggest you to run the app with --no-grid and redirect it to some path with  e.g:
    python3 ./passlistmaker.py --no-grid pass.txt
    you can also see the help menu with -h
    """
    for i in intro:
        print(i,sep='',end='',flush=1)
        sleep(0.02)       
    exit()

dinamit = []
common_passwrods = [
    '123456',
    '123456789',
    'Qwerty',
    'Password',
    '12345',
    '12345678',
    '111111',
    '1234567',
    '123123',
    'Qwerty123',
    '1q2w3e',
    '1234567890',
    'DEFAULT',
    '0',
    'Abc123',
    '654321',
    '123321',
    'Qwertyuiop',
    'Iloveyou',
    '666666',
]
passw_list = []
input_passwords = []


print()
a = input('add some clue : ')
b=a.split(' ')
for i in b:
    input_passwords.append(i)
print(f'got {a}, {input_passwords} added to clues ! ! !')
for i in input_passwords:
    passw_list.append(i)
    dinamit.append(i)


a=input('do you want to add most 20 common password to your passlist? (y/n)')
if a.lower() != 'n':
    for i in common_passwrods:
        passw_list.append(i)
a=input('do you want to add most 20 common password to your combine list? (y/n)')
if a.lower() != 'n':
    for i in common_passwrods:
        dinamit.append(i)

a=input('do you want to add all 8 digit numbers?(its consume about 8Gb ram) (y/n)')
if a.lower() == 'y':
    print('it can take a few minutes  ! ! !')
    for i in range (100000000):
        i = str(i)
        i2 = '0'* (len(i)-8)
        passw_list.append(f'{i2}{i}'
        )

a = input('do you want to add first 10M numbers to your pass combine list? (y/n)')
if a.lower() == 'y':
    for i in range (10000000):
        dinamit.append(str(i))

print('select combine groups length, huge number create stronger passlist but consume more resources and take more time')
a = input('2~5 (default is 2)')
if int(a) > 1 and int(a)<6:
    depths = int(a)
else:
    depths = 2


deraza = len(dinamit)
if depths > 1:
    for i in range(deraza):
        for j in range(deraza):
            passw_list.append(f'{dinamit[i]}-{dinamit[j]}')
            passw_list.append(f'{dinamit[i]}{dinamit[j]}')
if depths > 2:
    for i in range(deraza):
        for j in range(deraza):
            for g in range(deraza):
                passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}')
                passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}')
if depths > 3:
    for i in range(deraza):
        for j in range(deraza):
            for g in range(deraza):
                for g2 in range(deraza):
                    passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}-{dinamit[g2]}')
                    passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}{dinamit[g2]}')
if depths > 4:
    for i in range(deraza):
        for j in range(deraza):
            for g in range(deraza):
                for g2 in range(deraza):
                    for g3 in range(deraza):
                        passw_list.append(f'{dinamit[i]}-{dinamit[j]}-{dinamit[g]}-{dinamit[g2]}-{dinamit[g3]}')
                        passw_list.append(f'{dinamit[i]}{dinamit[j]}{dinamit[g]}{dinamit[g2]}{dinamit[g3]}')

"""
marboot be khrooji
"""

terminal_input = sys.argv[-1]
    

if '--no-grid' in sys.argv[-1:0:-1]:
    for i in passw_list:
        print(i)
elif '-w' in sys.argv[-1:0:-1]:
    file_path = sys.argv[(sys.argv.index('-w'))+1]
    try:
        with open(f'{file_path}/pass_list.txt', 'w+') as f:
            for i in passw_list:
                f.write(i)
                f.write('\n')
    except:
        os.system(f'mkdir -p {file_path}')
        with open(f'{file_path}/pass_list.txt', 'w+') as f:
            for i in passw_list:
                f.write(i)
                f.write('\n')
else:
    i = 0
    while True:
        if i % 5 == 0:
            print()
        try:
            grid =(30 - (len(passw_list[i]))) * ' '
            print(passw_list[i], end=f'{grid}')
        except IndexError:
            break
        i += 1
    print()
