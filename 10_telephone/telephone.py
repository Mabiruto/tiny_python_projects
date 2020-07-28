#!/usr/bin/env python3
"""
Author : mabiruto <mabiruto@localhost>
Date   : 2020-07-07
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import string
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent randomness',
                        metavar='float',
                        type=float, default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed',
                        metavar='int',
                        type=int, default = None)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    if not 0 <= args.mutations < 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1.')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text
    seed_arg = args.seed
    random.seed(args.seed)
    print(f'You said: "{text_arg}"')
    num_mutations = round(len(text_arg) * args.mutations)
    all_chars = ''.join(sorted(string.ascii_letters + string.punctuation))
    for index in random.sample(range(len(text_arg)), num_mutations):
        new_char = random.choice(all_chars.replace(text_arg[index], ''))
        text_arg = text_arg[:index] + new_char + text_arg[index + 1:]
    
    """
    new_text = ''
    chars_to_mutate = random.sample(range(len(text_arg)), num_mutations)
    for num in range(len(text_arg)):
        new_text += random.choice(all_chars.replace(text_arg[num], '')) if num in chars_to_mutate else text_arg[num]

    print(f'I heard : "{new_text}"')
    """
    print(f'I heard : "{text_arg}"')
# --------------------------------------------------
if __name__ == '__main__':
    main()
