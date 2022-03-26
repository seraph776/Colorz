#!/usr/bin/env python3
"""
created: 2022-03-26 12:29:25
@author: seraph★776
contact: seraph776@gmail.com
"""


class Colorz:
    """Colorz class"""

    # Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[34m'
    YELLOW = '\033[93m'
    VIOLET = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLACK = '\033[30m'
    WHITE = '\033[37m'

    # Background
    On_Black = '\033[40m'  # Black
    On_Red = "\033[41m"  # Red
    On_Green = "\033[42m"  # Green
    On_Yellow = "\033[43m"  # Yellow
    On_Blue = "\033[44m"  # Blue
    On_Purple = "\033[45m"  # Purple
    On_Cyan = "\033[46m"  # Cyan
    On_White = "\033[47m"  # White

    # Styles:
    BOLD = '\033[1m'
    ITALICS = '\033[3m'
    UNDERLINED = '\033[4m'
    STRIKE_THRU = '\033[9m'
    REVERSE = '\033[7m'
    END = '\033[0m'

    COLORS = [
        RED,
        GREEN,
        BLUE,
        YELLOW,
        VIOLET,
        PURPLE,
        CYAN,
        BLACK,
        WHITE,
        BOLD,
        ITALICS,
        UNDERLINED,
        STRIKE_THRU,
        REVERSE
    ]

    @staticmethod
    def red(text):
        return Colorz.RED + text + Colorz.END

    @staticmethod
    def green(text):
        return Colorz.GREEN + text + Colorz.END

    @staticmethod
    def blue(text):
        return Colorz.BLUE + text + Colorz.END

    @staticmethod
    def yellow(text):
        return Colorz.YELLOW + text + Colorz.END

    @staticmethod
    def violet(text):
        return Colorz.VIOLET + text + Colorz.END

    @staticmethod
    def purple(text):
        return Colorz.PURPLE + text + Colorz.END

    @staticmethod
    def cyan(text):
        return Colorz.CYAN + text + Colorz.END

    @staticmethod
    def black(text):
        return Colorz.BLACK + text + Colorz.END

    @staticmethod
    def display_colorz():
        print("-- Available Colors --")
        available_colors = ['RED',
                            'GREEN',
                            'BLUE',
                            'YELLOW',
                            'VIOLET',
                            'PURPLE',
                            'CYAN',
                            'BLACK',
                            'WHITE',
                            'BOLD',
                            'ITALICS',
                            'UNDERLINED',
                            'STRIKE_THRU',
                            'REVERSE']

        for i, color in enumerate(Colorz.COLORS):
            print(f" {Colorz.COLORS[i]} {i} {available_colors[i].title()} {Colorz.END}")


