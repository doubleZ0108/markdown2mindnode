#!/usr/bin/env python

import pyperclip
import os
import sys

def markdown_refactor_to_mindnode(file):
    refactor_strs = []
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f :
            list_symbol_index = line.find('-')
            num_of_space = list_symbol_index * 2
            newline = ''.join([' '] * num_of_space) + line.replace('-', ' ').lstrip()
            refactor_strs.append(newline)
    return refactor_strs

def save_to_clipboard(file):
    refactor_strs = markdown_refactor_to_mindnode(file)
    str = ''.join(refactor_strs)
    pyperclip.copy(str)
    print("Successfully saved to clipboard!")

def save_as_refactored_file(file):
    index = file.find('.')
    name = file[:index]
    appidx = os.path.splitext(file)[-1]
    newfile = name + '_refactor' + appidx

    refactor_strs = markdown_refactor_to_mindnode(file)

    with open(newfile, mode='w', encoding='utf-8') as f:
        for line in refactor_strs:
            f.write(line)
    print("Successfully saved to " + newfile + '!')

if __name__ == '__main__':
    file = '#'
    try:
        if len(sys.argv) > 3:   # there is Space in filename
            if sys.argv[-1] in ('file', 'clipboard'):
                file = ' '.join(sys.argv[1:-1])
            else:
                file = ' '.join(sys.argv[1:])
        else:
            file = sys.argv[1]
    except Exception:
        print("You must provide a .md file!")
    finally:
        if file != '#':
            try:
                mode = sys.argv[-1]
                if mode.find('.md') != -1:  # actually don't provide the second param
                    raise Exception
            except Exception:
                mode = 'clipboard'
                print("By default, the transformed content is copied to clipboard.")
            finally:
                if mode == 'clipboard':
                    save_to_clipboard(file)
                elif mode == 'file':
                    save_as_refactored_file(file)
                else:
                    print("The second parameter option is [clipboard | file], copy to clipboard by default.")
                    save_to_clipboard(file)
    # file = '/Users/doublez/Downloads/README.md'
    # markdown_refactor_to_mindnode(file)