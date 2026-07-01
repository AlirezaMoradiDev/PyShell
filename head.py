from sys import argv, exit
from os import path
from pathlib import Path
from exceptions import exception
file = open('test.txt', 'r')
lst = file.readlines()
print(lst)
file.close()
def main():
    """
    head.py <file(s)> <mode[optional]> <count[optional]>
    :return:
    """
    modes = {
        '-n': 'line',
        '-c': 'bytes'
    }
    if not path.isfile(argv[1]):    #is it a file or no?
        raise exception.NotFile

    with open(argv[1]) as file:
        try:
            mode = modes[argv[2]]
        except IndexError:
            mode = 'line'

        if mode == 'line':
            lines = file.readlines()
            counter = 1
            try:
                num = int(argv[3])
            except IndexError:
                num = 10
            try:
                while counter <= num:
                    print(f'{counter} {lines[counter - 1]}\n')
                    counter += 1
            except IndexError:
                print(f'file has {len(lines)} line')

        elif mode == 'bytes':
            counter = 0
            words = ''.join(file.readlines())
            try:
                n = int(argv[3])
                try:
                    while counter <= n:
                        print(words[counter], end='')
                        counter += 1
                except IndexError:
                    print(f'\nError: file has {len(words)} bytes')
            except IndexError:
                 print('To use the -c format, you must also enter the value.')

main()


