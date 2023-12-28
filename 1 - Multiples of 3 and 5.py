import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    soma = 0
    soma += (3 + (((n-1)//3)*3)) * ((n-1)//3) // 2
    soma += (5 + (((n-1)//5)*5)) * ((n-1)//5) // 2
    soma -= (15 + (((n-1)//15)*15)) * ((n-1)//15) // 2
    print(soma)