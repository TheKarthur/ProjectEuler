import sys

def num(n):
    a = n
    l = [i for i in range(1, n+1, 1)]
    
    while 1:
        c=0
        for x in l:
            if a % x:
                c+=1
                break
        if c == 0:
            return a
        a += 1
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(num(n))
