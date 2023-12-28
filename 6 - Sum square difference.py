import sys

def diff_square(n):
    aux = 0
    aux2 = 0
    for x in range(1, n+1):
        aux += x**2
    aux2 = (((1 + n) * n) // 2)**2
    return abs(aux - aux2)
        


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(diff_square(n))