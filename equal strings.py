for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    s=""
    for i in range(len(a)):
        if a[i]!=b[i]:
            s=s+b[i]
    print(len(set(s)))
            
            
        
