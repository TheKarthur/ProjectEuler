import sys

def fibo(n):
    f=[0, 1]
    while 1:
        if (f[-1] + f[-2] <= n):
            f.append(f[-1]+f[-2])
        else:
            return sum(x if x % 2 ==0 else 0 for x in f)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fibo(n))
