#!/usr/bin/env python3
"""
Author : Max Rubin-Toles <maxonbion@gmail.com>
Date   : 2020-08-03
Purpose: Mad Libs
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs for testing',
                        nargs='*',
                        metavar='str',
                        type=str,
                        default=[])

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    text = args.file.read().rstrip()
    search = re.findall('(<([^<>]+?)>)', text)
    placeholders = len(search)
    if not placeholders:
        print(f'"{args.file.name}" has no placeholders.', file=sys.stderr)
        sys.exit(1)
    inputs = args.inputs
    if not inputs:
        for pair in search:
            word = pair[1]
            if re.match('[aeiouAEIOU]', word):
                inputs.append(input(f'Give me an {word}: '))
            else:
                inputs.append(input(f'Give me a {word}: '))
    for num in range(placeholders):
        placeholder = search[num][0]
        text = re.sub(placeholder, inputs[num], text, count=1)
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()