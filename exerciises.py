def rotated_left(s):
    return s[1:]+s[0:1]

def rotated_right(s):
    return s[-1:-2:-1]+s[:-1]

#https://ru.hexlet.io/courses/python-lists/lessons/for-loop/exercise_unit
def find_index(value, source):
    if source is None:
        return None
    for i,x in enumerate(source):
        if x == value:
            print('>>>', i)
            return i
    else:
        return None

#https://ru.hexlet.io/courses/python-lists/lessons/iterators/exercise_unit
def find_second_index(value, items):
    i1 = find_index(value, items)
    if i1 is not None:
        i2 = find_index(value, items[i1+1:])
    else:
        i2 = None
    return i1+i2+1 if i2 is not None else None


#print(find_second_index('a', 'abcdead'))
#print(find_second_index('n', 'banana'))
#print(find_second_index('n', 'cannon'))

#assert find_second_index('!', '') is None
#assert find_second_index('!', '!') is None
#assert find_second_index(False, None) is None
#assert find_second_index('n', 'clone') is None
#assert find_second_index('n', 'banana') == 4
#assert find_second_index('n', 'cannon') == 3

def  hamming_weight(num):
    out = 0
    for x in bin(num):
        if x != '1':
            continue
        out += 1
    return out

#print(hamming_weight(101))

def triangle(n, back=0):
    line = []
    number = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            #print(number, end=" ")
            line.append(number)
            number += 1
        #print()    
    """
    line = []
    if n > 4:
        line = []
        p=triangle(n-1,back=1)
        s=0
        for i in range(1, n+2):
            x= p[i]
            s+= x
            if x == 1:
                line.append(x)
                s=x
            else:
                line.append(s+x)
                s=x
    else:
        for item in range(1, n+2):
            if item == 1 or item == n+1:
                line.append(1)
            elif item < n+1:
                if item%2 == 0 or (n-item)%2==0:
                    line.append(n)
                elif item%2 == 1:
                    line.append((n+2))
            elif item < n:
                line.append(n-1)
    """
    if back == 1:
        return line
    else:
        return '%s:%s' % (n,' '.join([str(x)for x in line]))
    
print(triangle(0))
print(triangle(1))
print(triangle(2))
print(triangle(3))
print(triangle(4))
print(triangle(5))
#print(triangle(6))
