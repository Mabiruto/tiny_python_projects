#!/usr/bin/env python3
"""
Author : mabiruto <mabiruto@localhost>
Date   : 2020-08-03
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


#---------------------------------------------------
def test_scramble():
    """Test scramble"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


#---------------------------------------------------
def scramble(word):
    if len(word) >= 4 and re.match('[a-zA-Z]', word):
        mid_lst = list(word[1:-1])
        random.shuffle(mid_lst)
        scr_mid = ''.join(mid_lst)

        word = f'{word[0]}{scr_mid}{word[-1]}'
    return word


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    for line in args.text.splitlines():
        split = splitter.split(line)
        words = [scramble(word) for word in split]
        print(''.join(words))


# --------------------------------------------------
if __name__ == '__main__':
    main()