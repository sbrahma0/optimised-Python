# Sum of the pairs which gives the taget Sum
# Brute force is avoided since it is O(n^2) complexity so here 1 applroach is usinh hash table and other is normal

# Time complexity O(n)
# Space complexity O(n)
def by_hash_table(array, targer):
    ht = {}
    for i in range(len(array)):
        if array[i] in ht:
            print(str(ht[array[i]])+'+'+str(array[i]))
            print(ht)
            return True
        else:
            ht[target-array[i]] = array[i]
    print(ht)
    return False

# Time complexity O(n)
# Space complexity O(1)
def optimised(array, target):
    i = 0
    j = len(array)-1
    while i<=j:
        if array[i]+array[j] == target:
            print(str(array[i])+'+'+str(array[j]))
            return True
        else:
            if array[i]+array[j] > target:
                j -= 1
            elif array[i]+array[j] < target:
                i += 1
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(by_hash_table(A,target))
print('****************')
print(optimised(A,target))
