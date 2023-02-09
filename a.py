a=int(input())
b=int(input())
mn=a if a<b else b
#print(mn)
for i in range(1, mn+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)
