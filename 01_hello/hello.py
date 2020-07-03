#!/usr/bin/env python3
"""
Author : mabiruto <mabiruto@localhost>
Date   : 2020-06-23
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--name',
                        help='Name to greet',
                        metavar='name',
                        type=str,
                        default='World')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print("Hello, " + args.name + "!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
