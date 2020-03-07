'''
This function return the 1st pair whose sum is nearest to the given target
'''
def closes_sum_pair(a1,a2,target):
    a1_sorted = sorted(a1)
    a2_sorted = sorted(a2)
    smallest_diff = abs(a1_sorted[0]+a2_sorted[0]-target)
    colses_pair = [a1_sorted[0],a2_sorted[0]]
    # starting from top right extream
    i = len(a1_sorted)-1 # This is to change the column index
    j = 0 # This is to change the row index
    
    # assuming a1 is at the top and a2 is at the left
    while (j<len(a1_sorted)) and i>=0 :
        current_diff = a1_sorted[j]+a2_sorted[i]-target
        if abs(current_diff)<smallest_diff:
            smallest_diff = abs(current_diff)
            closes_sum_pair = [a1_sorted[j],a2_sorted[i]]
            print (closes_sum_pair)
        
        if current_diff == 0:
            return [a1_sorted[j],a2_sorted[i]]

        elif current_diff <0:
            j = j+1
            
        elif current_diff > 0:
            i = i-1
    
    return closes_sum_pair

'''
This function return the all the pairs whose sum is nearest to the given target, and if the sum is equal to the target it will display only that pait
'''
'''
def closes_sum_pair(a1,a2,target):
    a1_sorted = sorted(a1)
    a2_sorted = sorted(a2)
    smallest_diff = abs(a1_sorted[0]+a2_sorted[0]-target)
    colses_pair = [a1_sorted[0],a2_sorted[0]]
    green = []
    # starting from top right extream
    i = len(a1_sorted)-1 # This is to change the column index
    j = 0 # This is to change the row index
    
    # assuming a1 is at the top and a2 is at the left
    while (j<len(a1_sorted)) and i>=0 :
        current_diff = a1_sorted[j]+a2_sorted[i]-target
        if abs(current_diff)<=smallest_diff:
            smallest_diff = abs(current_diff)
            closes_sum_pair = [a1_sorted[j],a2_sorted[i]]
            print (closes_sum_pair)
            
        if smallest_diff < 2 and closes_sum_pair not in green:
            green.append(closes_sum_pair)
        
        if current_diff == 0:
            return [a1_sorted[j],a2_sorted[i]]

        elif current_diff <0:
            j = j+1
            
        elif current_diff > 0:
            i = i-1
    
    return green
'''


# Driver
a1 = [-1, 3, 8, 2, 9, 5]
a2 = [4, 1, 2, 10, 5, 20]
a_target = 23
print('********',closes_sum_pair(a1, a2, a_target)) #should return (5, 20) or (3, 20).
