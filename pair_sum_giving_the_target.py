'''
def fun(lis,num):
    pair = []
    #sorted(lis)
    for i in range(len(lis)):
        for j in range(len(lis)):
            if j !=i and lis[i]+lis[j] == num:
                pair = [lis[i],lis[j]]
    
    return pair
'''
'''
def fun2(lis,num):
    seen = set()
    pair = []
    for n in lis:
        if num-n in seen:
            pair = [num-n, n]
        
        seen.add(n)
    
    return pair
'''

# by using the bisect function
from bisect import bisect_left


def fun3(lst, K):
    lst.sort()
    pair = []
    for i in range(len(lst)):
        target = K - lst[i]
        j = binary_search(lst, target)

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
        #  if there's another number that's the same value as lst[i] (since this is a sorted array so repeated numbers will be next to each other).
        
        if j == -1:
            continue
        elif j != i:
            pair = [lst[i],lst[j]]
            print([lst[i],lst[j]])
            return True
        elif j + 1 < len(lst) and lst[j + 1] == target:
            pair = [lst[i],lst[j+1]]
            print([lst[i],lst[j+1]])
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            pair = [lst[i],lst[j-1]]
            print([lst[i],lst[j-1]])
            return True
    print(pair)
    return False

def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)

    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1
    
# Driver

a = [10, 15, 3, 7] 
b = 17
print(fun3(a,b))
