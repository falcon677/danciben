# -*- coding: utf-8 -*-  

import bofang
import xiazai
import sys
import os
from optparse import OptionParser

USAGE = "usage:    python manage.py [read_file] [download_word] [langdu_word] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-l", dest="langdu")
parser.add_option("-d", dest="xiazai")
opt, args = parser.parse_args()

if len(args) < 1:
    print(USAGE)
    sys.exit(1)


def download_word(download_word):
    xiazai.download_yinpin(download_word)

def langdu_word():
    words = os.listdir('yinpin')
    bofang.bofang(words)

def read_file():
    words = []
    with open('danciben', 'r') as f:
        for word in f:
            words.append(word.replace("\n", ""))            

    download_word(words)


if __name__ == '__main__':

    for func in args:
        func = "%s()" % func
        print func
        eval(func)
