from os import path
from exceptions import exception
from sys import argv, exit

def main():
    modes = {
        '-n': 'line',
        '-c': 'bytes'
    }
    if not path.isfile(argv[1]):
        raise exception.NotFile

    with open(argv[1], 'r') as file:
        lines = file.readlines()
        try:
            mode = modes[argv[2]]
        except IndexError:
            mode = 'line'

        if mode == 'line':
            try:
                num = int(argv[3])
                counter = len(lines) - num
            except IndexError:
                num = 10
            try:
                while counter <= len(lines):
                    print(f'line {counter} of {len(lines)}: {lines[counter - 1]}\n')
                    counter += 1
            except IndexError:
                print(f'file has {len(lines)} line')

        elif mode == 'byte':
            pass
            sens = ''.join(lines)
            try:
                if int(argv[3]) > len(sens):
                    exit(f'The file has {len(sens)}-bit characters, but you gave {argv[3]} bits.')
                counter = len(sens) - int(argv[3]) + 1
                while counter < len(sens):
                    print(sens[counter], end='')
                    counter += 1
            except IndexError:
                print('To use the -c format, you must also enter the value.')


main()

