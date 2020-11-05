# Knapsack
# Method1 - Resursion

def knapsack(val, wt, capacity_left, index):
    #print("capacity left- ",capacity_left,"index- ",index)
    if capacity_left==0 or index == 0:
        result = 0
    
    elif capacity_left < wt[index-1]:
        result = knapsack(val, wt, capacity_left, index-1)
    
    else:
        temp1 = knapsack(val, wt, capacity_left, index-1) # not considering current item
        temp2 = val[index-1] + knapsack(val, wt, capacity_left-wt[index-1], index-1)
        result = max(temp1, temp2)
    #print("Result- ",result)
    return result
    
wt = [5,4,6,3]
val = [10,40,30,50]
capacity = 10
index = len(wt)
print(knapsack(val, wt, capacity, index))
