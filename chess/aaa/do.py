#!/usr/bin/env python3
# coding: UTF-8

import random
import re

# [駒][リードFILR][リードRANK][駒取得(x)][取得した駒][FILE(縦)][RANK(横)][プロモーション][アンパッサン][チェック・チェックメイト]

class Banmen:
    def hyouzi(utu, FILE, RANK):
#        print("  a b c d e f g h")
        print("  a  b  c  d  e  f  g  h")
#        print(" -----------------")
        print(" -------------------------")
        for rank in range(8):
            print("{}|".format(8 - rank), end="")
            for file in range(8):
                if str(board[rank][file]) == '0':
                    print("  |", end="")

                elif str('-') in str(board[rank][file]) != True:
                    print('\033[31m' + str(board[rank][file]).replace('-', '') + '\033[0m' + " |", end="")

                else:
                    print(str(board[rank][file]) + " |", end="")

            print(8 - rank)
#        print(" -----------------")
            print(" -------------------------")
#        print("  a b c d e f g h")
        print("  a  b  c  d  e  f  g  h")
        print("{0}{1}{2}".format(utu, FILE, (8 - RANK)))




if __name__ == "__main__":
    board = [
            ['-R', '-N', '-B', '-Q', '-K', '-B', '-N', '-R'],
            ['-P', '-P', '-P', '-P', '-P', '-P', '-P', '-P'],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
            ]

    File = random.randint(0, 7)
    Rank = random.randint(0, 7)
    Files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    a = input("GO -> ")
    board[File][Rank] = a
    Banmen.hyouzi(a, Files[File], Rank)

