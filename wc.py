from sys import argv, exit
from os import path
from exceptions import exception

def main():
    modes = {
        '-l': 'line',
        '-c': 'bytes', 
        '-w': 'word'
    }
    try:
        if not path.isfile(argv[1]):    #is it a file or no?     #py test.txt
            raise IndexError(f'{argv[1]} is not file format... ')

        with open(argv[1], 'r') as file:
            lines = file.readlines()
            try:
                mode = modes[argv[2]]
            except IndexError:
                mode = 'line'

                
            if mode == 'line':
                print(len(lines))

            elif mode == 'word':
                n_word = (''.join(lines).split())
                print(len(n_word))

            elif mode == 'bytes':
                n_byte = len(''.join(lines))
                print(n_byte)
        
    except IndexError:
            lst = []
            while True:
                text = input('Enter text: ')
                if text == '':
                    break
                else: 
                    with_space = text + ' '
                    lst.append(with_space)

            n_line = len(lst)
            n_word = len(''.join(lst).split())
            n_byte = len(''.join(lst))
            print(f'{n_line} {n_word} {n_byte}')
            
main()