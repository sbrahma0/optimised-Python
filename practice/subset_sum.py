# This is an example of recursive function
# https://youtu.be/nqlNzOcnCfs
def count_subsets(a,t):
    return recur(a,t,len(a)-1)

def recur(a,t,i):
    if t==0:
        return 1
    elif t<0 or i<0:
        return 0
    elif t<a[i]:
        return recur(a,t,i-1)
    else:
        return recur(a,t-a[i],i-1) + recur(a,t,i-1)

'''
# For dynamic programming solution or memoised
def count_subsets(a,t):
    mem = {}
    return recur(a,t,len(a)-1,mem)

def recur(a,t,i,mem):
    key = str(t)+":"+str(i)
    if key in mem:
        return mem[key]
    elif t==0:
        return 1
    elif t<0 or i<0:
        return 0
    elif t<a[i]:
        key_value = recur(a,t,i-1,mem)
    else:
        key_value = recur(a,t-a[i],i-1,mem) + recur(a,t,i-1,mem)
    
    mem[key] = key_value
    return key_value
'''
a = [2,4,6,10]
target = 16

print(count_subsets(a,target))
