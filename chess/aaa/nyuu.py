#!/usr/bin/env python3
# coding: UTF-8

import re


# [駒][リードFILE][リードRANK][駒取得(x)][取得した駒][FILE(縦)][RANK(横)][プロモーション][アンパッサン][チェック・チェックメイト]
# [キャスリング]


def kihu(kihu):
    go = re.match(r"^[PBNRQK]?[a-h]?[1-8]?x?[a-h][1-8](=[BNRQK]|(e.p.))?[\+#]?", kihu)

    if go:
        kihu = go.group()
        print(kihu)

        if kihu[0] in ['B' ,'N', 'R', 'Q', 'K']:
            koma = kihu[0]
            kihu = re.sub('[BNRQKx\+#]', '', kihu)
            print(koma, kihu)

        else:
            kihu = re.sub('[Px\+#]', '', kihu)
            print("pawn", kihu)        

    elif kihu == 'o-o-o' or kihu == 'O-O-O' or kihu == '0-0-0':
        print('Q-side castling')

    elif kihu == 'o-o' or kihu == 'O-O' or kihu == '0-0':
        print("K-side castling")

    elif kihu == '1-0':
        print("White win")

    elif kihu == '0-1':
        print("Black win")
    
    elif kihu == '1/2-1/2':
        print("Draw")

    else:
        print("Wrong")


if __name__ == "__main__":
    aaa = input("GO -> ")
    kihu(aaa)
