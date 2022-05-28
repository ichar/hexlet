from collections import Counter


def visualize(data, bar_char='₽'):
    #print('-0-')
    ctr = Counter(data)
    outs = []
    cols = []
    w = 2
    smb = bar_char * (w)
    mask = f'%-{w}d'
    total = 0
    #print('-1-')
    for key, cnt in sorted(ctr.most_common()):
        col = []
        total += key*cnt
        col.append(mask % key)
        col.append('-'*(w+1))
        col += [smb for i in range(0,cnt)]
        col.append(mask % cnt)
        cols.append(col)
        #line = ''.join([str(x) for x in col])
        #out.append(line)
    #print('-2-')
    lines = 0
    columns = len(ctr)
    for x in cols:
        l = len(x)
        #print(x, ':', l)
        lines = max(lines, l)

    #print(f"{lines} lines*{columns} columns, Total:{total}.")
    #print(cols)

    for line in range(lines,0,-1):
        #print(line)
        out = ""
        for col in cols:
            if len(col) < line:
                out += ' '*(w+1)
            else:
                out += str(col[line-1])
                if not out.endswith('-'):
                    out += ' '

        outs.append(out)
  
    size=len(outs[-1])-1
  
    return '\n'.join([(s+''*10)[0:size] for s in outs])
  

"""
image = visualize((1, 2, 3, 5, 10, 20, 15, 10, 5, 3, 2, 1, 5, 10, 2, 15, 15, 15), '*')
#for x in image:
#  print(x)
print(image)
print('ok')
"""

MONEY = (1, 20, 2, 5, 20, 3, 5, 2, 10, 2, 20, 2, 20, 1, 2, 1, 1, 2, 10, 20, 3,)
image = visualize(MONEY,'₽')
print(image)

assert visualize(MONEY) == """
   6             
   ₽₽          5 
4  ₽₽          ₽₽
₽₽ ₽₽          ₽₽
₽₽ ₽₽ 2  2  2  ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
-----------------
1  2  3  5  10 20
"""[1:-1]

image = visualize(MONEY,'$')
print(image)
assert visualize(MONEY, bar_char='$') == """
   6             
   $$          5 
4  $$          $$
$$ $$          $$
$$ $$ 2  2  2  $$
$$ $$ $$ $$ $$ $$
$$ $$ $$ $$ $$ $$
-----------------
1  2  3  5  10 20
"""[1:-1]
