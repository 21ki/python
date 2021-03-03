#! /usr/bin/env python

import subprocess
import os
import time

isso_dir = '/opt/isso/db/'

def subprocess_():
    os.chdir(isso_dir)
    try:
        subprocess.check_call('tar -zcvf comments.tar.gz comments.db', shell=True)
    except:
        exit(1)
    try:
        subprocess.check_call('git add .', shell=True)
    except:
        exit(2)
    try:
        subprocess.check_call('git commit -m "backup at %s"' % time.ctime(), shell=True)
    except:
        exit(3)
    try:
        subprocess.check_call('git push -u origin master', shell=True)
    except:
        exit(4)
    print "success at: %s" % time.ctime()



def main():
    subprocess_()

if __name__ == '__main__':
    main()
