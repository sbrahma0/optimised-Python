#https://youtu.be/nqlNzOcnCfs

def no_of_sets(arr, total):
    memo = {}
    return recursive(arr, total, len(arr)-1, memo)

def recursive(arr, total, i, memo):
    key = str(total)+":"+str(i)
    if key in memo:
        return memo[key]
    if total == 0:
        return 1
    
    elif total < 0:
        return 0
    
    elif i < 0:
        return 0
    
    elif total<arr[i]:
        assign = recursive(arr, total, i-1, memo)
    
    else:
        assign = recursive(arr, total, i-1, memo) + recursive(arr, total-arr[i], i-1, memo)
    
    memo[key] = assign
    return assign

# driver
a = [2,4,6,10]
print(no_of_sets(a,10))
