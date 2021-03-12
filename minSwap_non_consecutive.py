# different from non consecutive and not efficient for it too, see the code for consecutive one in minSwap_consecutive.py

def minswap(arr):
    count = 0
    min_loc = 0
    for i in range(len(arr)-1):
        min_loc = i
        
        for j in range(i, len(arr)):
            if arr[j]<arr[min_loc]:
                min_loc = j
        
        if min_loc != i:
            arr[min_loc], arr[i] = arr[i], arr[min_loc]
            count += 1
    
    print(count)


a = [4,2,1,9]
minswap(a)
