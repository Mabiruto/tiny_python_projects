#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Purpose: Python program to write a Python program
"""

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('str', help='any string', type=str)
    args = parser.parse_args()
    answer = ''
    for num in range(len(args.str)):
        if args.str[num].isdigit():
            if int(args.str[num]) == 1:
                answer += str(9)
            if int(args.str[num]) == 2:
                answer += str(8)
            if int(args.str[num]) == 3:
                answer += str(7)
            if int(args.str[num]) == 4:
                answer += str(6)
            if int(args.str[num]) == 5:
                answer += str(0)
            if int(args.str[num]) == 6:
                answer += str(4)
            if int(args.str[num]) == 7:
                answer += str(3)
            if int(args.str[num]) == 8:
                answer += str(2)
            if int(args.str[num]) == 9:
                answer += str(1)
            if int(args.str[num]) == 0:
                answer += str(5)
        else:
            answer += args.str[num]
    print(answer)

if __name__ == '__main__':
    main()