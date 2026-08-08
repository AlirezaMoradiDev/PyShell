from sys import argv
from os import path
# from ..exceptions import exception

def main():
    """
    head.py <file> <mode[optional]> <count[optional]>
    :return:
    """
    if len(argv) < 2:
        raise IOError('Invalid input number')

    modes = {
        '-n': 'line',
        '-c': 'bytes'
    }
    if not path.isfile(argv[1]):    #is it a file or no?
        raise FileNotFoundError('file not found!')

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
                    print(f'line--> {counter}: {lines[counter - 1].rstrip()} \n')
                    counter += 1
            except IndexError:
                print(f'file has {len(lines)} line !')

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

if __name__ == "__main__":
    main()

