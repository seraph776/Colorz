#!/usr/bin/env python3
"""
created: 2022-03-26 12:57:43
@author: seraph★776
contact: seraph776@gmail.com
"""

from colorz import Colorz


def main():
    s1 = 'Hello world!'
    s2 = 'E=MC^2'
    print(Colorz.green(s1))
    print(Colorz.cyan(s2))
    print(Colorz.purple('Python programming'))


if __name__ == '__main__':
    main()
