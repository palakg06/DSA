def check(n,arr):
    arr.sort()
    t=arr[0]+arr[n-1]
    i = 0
    j = n - 1
    while (i<j):
        if (arr[i] + arr[j] == t):
            i += 1
            j -= 1
        else:
            return False
    return True
n =6
arr = [3,1,2,4,5,6]
b = check(n, arr)
print(b)  
    
