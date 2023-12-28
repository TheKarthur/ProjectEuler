import sys

def fun(n):
    for x in range(n-1, 101100, -1):
        if sum(int(y) for y in str(x)) % 2 == 0:
            if str(x)[:3] == str(x)[3:][::-1]:
                for h in range(int((x**0.5))+1, 99, -1):
                    if x % h == 0:
                        if len(str(int(x / h))) < 4:
                            return x

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fun(n))