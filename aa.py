def gcd(a,b):
 if b==0:
     return a
 else:
     return gcd(b,a%b)
for _ in range(int(input())):
    mingcd=1000000000
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-1):
        g=gcd(a[i],a[i+1])
        if g<mingcd:
            mingcd=g
    print(mingcd*n)
     
