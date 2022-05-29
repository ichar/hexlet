import sys


is_v3 = True if sys.version_info[0] > 2 else False


_VERSION_ = '1.0 Python3'

ISDEBUG = 0
ISTRACE = 1

def check(x):
    """
        Checks a number and print results or return it.
        
        Arguments:
            x -- int, nimber to check, x >= 0
        Returns:
            results string code as {Fizz|Buzz|FizzBuzz} or nothing (empty string)
    """
    out = ''
    if x <= 0:
        pass
    s= f"{x}:" if not ISDEBUG else ''
    if ISTRACE:
        print(f"Trace:{x}")
    if x%15 == 0:
        out=f"{s}FizzBuzz"
    elif x%5 == 0:
        out =f"{s}Buzz"
    elif x%3 == 0:
        out=f"{s}Fizz"

    if out:
        print(out)
    return out

def walk(v1, v2=0, **kw):
    """
        Iterates given numbersequences from v1 to v2 and shecks the result.
        
        Arguments:
            v1 -- int, start from this
            v2 -- int, finish to this
        Keyword arguments:
            debug -- bool or 1|0, set ISDEBUG option (prints prefered value to check in output such as 21:'21:Fizz')
            trace -- bool or 1|0, set ISTRACE option (prints script's trace output: Trace:....)

        Returns:
            out -- str: final script's result-string as join any given values to check specially for tests
    """
    global ISDEBUG, ISTRACE
    ISDEBUG=kw.get('debug', 0)
    ISTRACE=kw.get('trace', 0)
    out = []
    begin = v1 and v1 > 0 and v1 or 0
    end = v2>0 and v2+1 or v1+1
    for x in range(begin, end):
        out.append(check(x))

    out = [x for x in out if x]
    if ISTRACE:
        print('Trace:', out)
    return out

def interactive():
    """
        Runs interactive script mode
    """
    while True:
        x=input('Type an integer, please, or q for exit:')
        if x == 'q' or not x.isdigit():
            return
        check(int(x))

def test():
    """
        Inner tests (self-tests)
    """
    assert ':'.join(walk(0,12, debug=1)) == 'FizzBuzz:Fizz:Buzz:Fizz:Fizz:Buzz:Fizz'
    assert ':'.join(walk(100, debug=1, trace=0)) == 'Buzz'
 
    print('Test OK')

if __name__ == "__main__":
    argv = sys.argv


    if len(argv) == 1 or argv[1].lower() in ('/h', '-h', 'help', '--help', '/?'):
        print('--> FizzBuzz script')
        print('--> ')
        print('--> python3 fizzbuz.py [{-i|-c|-r|-t}] [start [finish]]')
        print('--> ')
        print('--> -i: interactive mode with type a number request')
        print('--> example:fizzbuz.py -i')
        print('--> ')
        print('--> -c: only check a given start value')
        print('--> example:fizzbuz.py -c 21')
        print('--> ')
        print('--> -r: walk through the values range from start to finish')
        print('--> example:fizzbuz.py -r 0 100 or fizzbuz.py 0 100')
        print('--> ')
        print('--> -t: tests')
        print('--> ')
        print('--> start and finish should be an integer number>=0.')
        print('--> ')
        print('--> %s' % _VERSION_)
    else:
        start = finish = None
        is_interact = 0
        is_check = 0
        is_range = 0
        is_test = 0
        for arg in argv[1:]:
            if arg.startswith('-'):
                if arg == '-i':
                    is_interact = 1
                if arg == '-c':
                    is_check = 1
                if arg == '-r':
                    is_range = 1
                if arg == '-t':
                    is_test = 1
            elif arg.isdigit():
                if start is None:
                    start=int(arg)
                elif is_range or not is_check:
                    finish=int(arg)
                    is_range = 1
                    is_check = 0

        if ISTRACE:
            print(f"Trace:{start}:{finish}")

        if is_test:
            test()
        elif is_interact:
            interactive()
        else:
            walk(start,finish or 0, trace=0)
