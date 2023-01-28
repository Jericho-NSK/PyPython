from simple_colors import *


def colored_cat():
    print(red('\t\t\t\t\t\t\t/\_/\\\n\t\t\t\t\t\t\t>^,^<'),
          yellow(' ___ PURR PURR'),
          cyan('\n\t\t\t\t\t\t\t / \\\n\t\t\t\t\t\t\t(|_|)_/\t\t'),
          green('/***\\', 'underlined'))


def monochrome_cat():
    print('\t\t\t\t\t\t\t/\_/\\\n'
          '\t\t\t\t\t\t\t>^,^< ___ MEOW!!!''\n'
          '\t\t\t\t\t\t\t / \\\n'
          '\t\t\t\t\t\t\t(|_|)_/\t\t''/___\\')


if __name__ == '__main__':
    colored_cat()
    monochrome_cat()
