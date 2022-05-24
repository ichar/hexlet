import sys
import os
import re


is_v3 = sys.version_info[0] > 2 and True or False


version = '1.0 Python3'

config = {}

EOL = '\n'

IsDebug = 0
IsTrace = 1

def check(x):
    if x%15 == 0:
        print f"{x}:FizzBuzz"
    elif x%5 == 0:
        print f"{x}:Buzz"
    if x%3 == 0:
        print f"{x}:Fizz"


def walk(v1, v2):
    for x in range(v1,v2>0 and v2 or v1+1):
        check(x)


if __name__ == "__main__":
    argv = sys.argv


    if len(argv) == 1 or argv[1].lower() in ('/h', '-h', 'help', '--help', '/?'):
        print('--> ')
        print('--> ')
        print('--> ')
        print('--> ')
        print('--> ')
        print('--> %s' % version)
    else:
        x1 = x2 = None
        is_interact = False
        is_check = False
        is_range = False
        for i in len(argv):
            arg = argv[i]
            if arg.startswith('-'):
                if arg == '-i':
                    is_interact = true
                if arg == '-c':
                    is_check = true
                if arg == '-r':
                    is_range = true
            else:
                if x1 is None:
                    x1=int(arg)
                else:
                    x2=int(arg)
                is_range = true

        walk(x1,x2)
