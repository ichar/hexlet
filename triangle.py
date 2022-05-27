IsTrace=0
def triangle(n):
  line = []
  rows=n+2
  if n > 4:
    p=triangle(n-1)
    s = 0
    for index in range(0, n+1):
      if index in (0, n):
        line.append(1)
        s=1
      else:
        s+=p[index]
        line.append(s)
        s=p[index]
      if IsTrace:
          print('>>>index:', index, s)
      
  else:
    for index in range(1, rows):
        if index == 1 or index == n+1:
            line.append(1)
        elif index < n+1:
            if index%2 == 0 or (n-index)%2==0:
                line.append(n)
            elif index%2 == 1:
                line.append(sum(line[0:index-1])+1)
        #elif index < n:
        #    line.append(n-1)
  return line

for x in range(1,15):
    print(triangle(x))
