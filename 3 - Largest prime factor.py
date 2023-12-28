import sys

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    a=2
    while n != 1:
        if n % a == 0:
            n /= a
        else:
            a += 1
        if a*a > n:
            a=n
            break
    print(int(a))
