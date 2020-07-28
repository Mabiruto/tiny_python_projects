#!/usr/bin/env python3
"""
Author : Max Rubin-Toles <maxonbion@gmail.com>
Date   : 2020-07-27
Purpose: Rhyme a given word
"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create rhyming words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='Word to rhyme', type=str)

    args = parser.parse_args()

    red_flag = 0

    for letter in args.word:
        if letter not in f'{string.ascii_lowercase}{string.ascii_uppercase}':
            red_flag += 1

    if red_flag != 0:
        parser.error(
            f' -word "{args.word}" must be composed only of English letters'
        )

    return args


#---------------------------------------------------
def test_stemmer():
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')


#---------------------------------------------------
def stemmer(word):
    str_1 = ''
    str_2 = ''
    arb_val = 0
    for letter in word:
        if letter in 'aeiouAEIOU':
            arb_val += 1
            str_2 += letter.lower()
        elif arb_val != 0:
            str_2 += letter.lower()
        else:
            str_1 += letter.lower()
    return (str_1, str_2)
    """
    consonants = ''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])
    match = re.match(f'([{consonants}]+)?(.*)', word.lower())
    return (match.group(1) or '', match.group(2) or '') if match else ('', '')
    """


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    consonants = ''.join(
        [c for c in string.ascii_lowercase if c not in 'aeiou'])
    prefixes = list(
        consonants
    ) + 'bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr'.split(
    )
    args = get_args()
    start, rest = stemmer(args.word)
    rhymes = '\n'.join(sorted([p + rest for p in prefixes if p != start]))
    if rest:
        print(rhymes)
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()