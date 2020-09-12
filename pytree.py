#!/usr/bin/python3


import os
import sys

CRED = '\033[91m'   # Color red
CEND = '\033[0m'    # Stop coloring


def get_list_of_items_in_folder(path):
    try:
        with os.scandir(path) as iterator:
            entries = [entry for entry in iterator]
    except NotADirectoryError:
        print("Not a directory")
        return []
    return entries

def go_and_print_childs(path, extension=''):
    entries = get_list_of_items_in_folder(path)

    entries.sort(key=lambda x: x.name, reverse=False)

    for index in range(len(entries)):
        if entries[index].is_file():
            if index == len(entries)-1: # end
                print(extension + u'\u2514 ' + entries[index].name)
            else: # in the mid
                print(extension + u'\u251C ' + entries[index].name)

        if entries[index].is_dir():
            if index == len(entries) - 1:
                print(extension + u'\u2514 ' + CRED + entries[index].name + CEND)
                go_and_print_childs(entries[index].path, extension + u'    ')
            else:
                print(extension + u'\u251C ' + CRED + entries[index].name + CEND)
                go_and_print_childs(entries[index].path, extension + u'\u2502   ')


def get_folder_abspath():
    try:
        folder_to_inspect = sys.argv[1]
    except IndexError:
        folder_to_inspect = '.'
    abs_path = os.path.abspath(folder_to_inspect)
    return abs_path

def main():
    root_node = get_folder_abspath()
    print(root_node)
    go_and_print_childs(root_node)

if __name__ == '__main__':
    main()
