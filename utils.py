from time import sleep
import sys
import os


def intro():
    print('tags:'
          '\n\r help,h,H,h*              show this help'
          '\n\r -w                       specify a directory to write the passlist to it'
          '\n\r --no-grid                make output in one line')
    print()
    text = """if you would like to save the pass to a file
    i suggest you to run the app with -w and specify a directory to save the passwords e.g:
    python3 ./passlistmaker.py -w passlist
    this will save the outputs on ./passlist/pass_list.txt
    you can also see the help menu with -h
    """
    for i in text:
        print(i, sep='', end='', flush=True)
        sleep(0.02)
    print()
    exit()


def print_to_terminal(passw_list):
    i = 0
    while True:
        if i % 5 == 0:
            print()
        try:
            grid = (30 - (len(passw_list[i]))) * ' '
            print(passw_list[i], end=f'{grid}')
        except IndexError:
            break
        i += 1
    print()


def write_to_file(passw_list):
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