import pygame
import subprocess



def bofang(words, times=5, rate=1.2):
    print "langdu"
    print words
    for word in words:
        word = 'yinpin/%s' % word
        sudo = rate
        for time in range(0, times):
            print time
            print word
            sudo = sudo + 0.1
            #subprocess.call(['afplay', '-r', '1.2', word])  
            subprocess.call(['afplay', '-r', str(sudo), word])
            

