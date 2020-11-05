# Knapsack
# Method 2 - Dynamic Tabular (Bottom UP)

def knapsack(val, wt, capacity, index):
    cache = [[0 for x in range(capacity+1)] for x in range(index+1)]
    
    for row in range(index+1):
        for col in range(capacity+1):
            
            if row==0 or col==0:
                cache[row][col] = 0

            elif wt[row-1]<=col:
                temp1 = val[row-1] + cache[row-1][col-wt[row-1]]
                temp2 = cache[row-1][col]
                #print("max- ",max(temp1, temp2))
                cache[row][col] = max(temp1, temp2)
            
            else:
                cache[row][col] = cache[row-1][col]
        #print(cache)
    return cache[-1][-1]
    
    
wt = [5,4,6,3]
val = [10,40,30,50]
capacity = 10
index = len(wt)
print(knapsack(val, wt, capacity, index))

