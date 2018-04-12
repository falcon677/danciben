import os
import sys
import requests 
import inspect


script_dir = os.path.join(os.path.dirname(inspect.stack()[-1][1]), 'yinpin')

def download_yinpin(dancis):
    print "down load pinyin to pinyin."
    print dancis
    for danci in dancis: 
        url = "http://dict.youdao.com/dictvoice?type=1&audio=%s" % danci 
        print url
        danci_yinpin_file =  os.path.join(script_dir, danci)
        
        print "downloading to %s " % danci_yinpin_file
        r = requests.get(url) 
        with open(danci_yinpin_file, "wb") as code:
            code.write(r.content)



if __name__ == "__main__":
    download_yinpin('world')
