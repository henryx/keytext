#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import collections
import sys

__author__ = "Enrico Bianchi"
__credits__ = ["Enrico Bianchi", ]
__license__ = "MIT"
__maintainer__ = "Enrico Bianchi"
__version__ = "1.0.0"


def init_args():
    """
    Argument parser initialization
    :return: An object that parse arguments passed from command line
    """

    args = argparse.ArgumentParser(description="keytext")
    args.add_argument("filename", help="File to parse")

    return args


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

    args = init_args().parse_args(sys.argv[1:])


if __name__ == '__main__':
    main()
