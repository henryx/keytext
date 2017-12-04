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
    distribution = {
        "layout": {
            "it": {
                "sx": {
                    "indice": ["%&56rtfgvb"],
                    "medio": ["$4edc"],
                    "anulare": ["3£wsx"],
                    "mignolo": ['<>qaz\\|1!2"']
                },
                "dx": {
                    "indice": ["/(78yuhjnm"],
                    "medio": [")9ik;,"],
                    "anulare": ["=0ol:."],
                    "mignolo": ["?'^ìpèé+*[]{}çò@°à#§ù-_"]
                }
            }
        }
    }

    fingers = collections.OrderedDict([
        ("indice", 0),
        ("medio", 0),
        ("anulare", 0),
        ("mignolo", 0)
    ])

    hand = {
        "dx": fingers.copy(),
        "sx": fingers.copy(),
        "spaces": 0
    }

    args = init_args().parse_args(sys.argv[1:])

    with open(args.filename) as filedata:
        for line in filedata:
            for character in line:
                if character == " ":
                    hand["spaces"] = hand["spaces"] + 1


if __name__ == '__main__':
    main()
