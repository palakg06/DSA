for _ in range(int(input())):
    n=int(input())
    s=input()
    l1=[]
    l2=[]
    for i in range(n):
        if i%2==0:
            l1.append(s[i])
        else:
            l2.append(s[i])
    l1.sort()
    l2.sort()
    if l1==l2:
        print('yes')
    else:
        print('no')
        
