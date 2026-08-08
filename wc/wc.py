from sys import argv, exit
from os import path


def main():
    modes = {
        '-l': 'line',
        '-c': 'bytes', 
        '-w': 'word',
        '-m': 'char',
        '-L': 'long line'
    }
    if len(argv) < 2:
        raise IOError('Invalid input number')
    try:
        if not path.isfile(argv[1]):    #is it a file or no?     #py test.txt
            raise IndexError(f'{argv[1]} is not file format... ')

        with open(argv[1], 'r', encoding='utf-8') as file:
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
                n_byte = len(''.join(lines).encode())
                print(f'{n_byte} {argv[1]}')

            elif mode == 'char':
                char = 0
                for words in lines:
                    for ch in words:
                        char += 1
                print(f'{char} {argv[1]}')

            elif mode == 'long line':
                mx = len(lines[0])
                counter = 1
                while counter < len(lines):
                    if len(lines[counter]) > mx:
                        mx = len(lines[counter])
                    counter += 1
                print(f'{mx} {argv[1]}')

    except IndexError:   # not file -> terminal mood
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