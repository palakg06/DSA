def divide(arr):
    if len(arr)==1:
        return arr
    half=len(arr)//2
    left=divide(arr[:half])
    right=divide(arr[half:])
    return conquer(left,right)
def conquer(arr1,arr2):
    result=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    while i<len(arr1):
        result.append(arr1[i])
        i+=1
    while j<len(arr2):
        result.append(arr2[j])
        j+=1
    return result
print(divide([8,7,6,5,4,3,2,1]))
