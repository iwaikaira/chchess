#!/usr/bin/env python3
# coding: UTF-8

import re
import nyuu

turn = 1

def change(tread, turn):
    tread = re.sub('[^PBNRQK0-8a-hx.poO\-\+#/]', '', tread)
    if turn > 0:
        return tread, -1
    else:
        return tread, 1

while(turn != 0):
    if turn > 0:
        white = input("白の手番 -> ")
        white, turn = change(white, turn)
        print(white)
        nyuu

    else:
        black = input("黒の手番 -> ")
        black, turn = change(black, turn)
        print(black)



print("決着ゥゥーーーッ！")
    
