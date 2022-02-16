#!/usr/bin/env python3
# coding: UTF-8

import re

def piece(kihu):
    af_F = kihu[-2]
    af_R = kihu[-1]
    print(af_F, af_R)
    if len(kihu) > 2:
        if kihu[0].isalpha() == True:
            be_F = kihu[0]

            if kihu[1].isalpha() == True:
                be_R = None
                af_F = kihu[1]
                af_R = kihu[2]
                print("al_al_nu")

            else:
                be_R = kihu[1]
                af_F = kihu[2]
                af_R = kihu[3]
                print("al_nu_al_nu")

        else:
            be_F = None
            be_R = kihu[0]
            af_F = kihu[1]
            af_R = kihu[2]
            print("nu_al_nu")
    
    else:
        be_F = None
        be_R = None
        af_F = kihu[0]
        af_R = kihu[1]

    return be_F, be_R, af_F, af_R


def pawn(kihu):
    print("PAWN")
    if 'e.p.' in kihu:
        print("anpa")

    elif '=' in kihu:
        print("pro")

    else :
        be_F, be_R, af_F, af_R = piece(kihu)



def sel(koma):
    if koma == 'B':
        print("bishop")

    elif koma == 'N':
        print("knight")

    elif koma == 'R':
        print("rook")

    elif koma == 'Q':
        print("queen")

    else:
        print("king")


def bishop(kihu):
    bishop


if __name__ == "__main__":
    a = input("koma")
    b = input("kihu")
#    piece(b)
    pawn(b)
