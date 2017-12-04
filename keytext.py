#!/usr/bin/python3
# -*- coding: utf-8 -*-

import collections

__author__ = "Enrico Bianchi"
__credits__ = ["Enrico Bianchi", ]
__license__ = "MIT"
__maintainer__ = "Enrico Bianchi"
__version__ = "1.0.0"


def main():
    """
    Main function
    """
    fingers = collections.OrderedDict([
        ("indice", 0),
        ("medio", 0),
        ("anulare", 0),
        ("mignolo", 0)
    ])

    hand = {
        "dx": fingers.copy(),
        "sx": fingers.copy(),
    }


if __name__ == '__main__':
    main()
