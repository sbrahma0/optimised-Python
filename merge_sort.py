
# Merge sort
# There are 2 finctions 1 for dividing the array and one for merging the elements.
# The sorting as per comparisons happen in the merge section.

def split(array):
    if len(array)>1:
        mid = len(array)//2
        left = array[:mid] # first till mid-1
        right = array[mid:] # mid to last
        print(left,"****",right)
        split(left)
        split(right)
        merge(left,right,array)
    

def merge(left, right, array):
    i=0 # This is to traverse the elements in the left array
    j=0 # This is to traverse the elements in the right array
    k=0 # This is to place the elements in the array
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        k+=1
        # Now prevoius loop will terminate when either of the traversing 
        # is complete thus making the other list partially traversed, thus 
        # We need to make another traversing loop for the incomplete traversed list
        
    while i<len(left):
        array[k] = left[i]
        i+=1
        k+=1
    while j<len(right):
        array[k] = right[j]
        #print('------',right[j])
        j+=1
        k+=1
    
array = [1,6,5,3,8,9,7,10]
split(array)
print(array)
