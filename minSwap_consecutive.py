# vid link - https://youtu.be/f7IIW0HVUcQ

# This is diff from adjacent swaps and if the numbers are not consecutive

def min_swaps(arr):
    hash = {element:index for index,element in enumerate(arr)} 
    
    total_swap_count=0
    visited = [False]*len(arr)
    
    for element, index in hash.items():
        if element==index or visited[element]: # if the element is in correct place or if is visited
            continue
        
        swap_count=0
        value=element
        while not visited[element]:
            visited[element]=True
            swap_count += 1
            element = hash[element]
        
        total_swap_count += swap_count-1
    
    return total_swap_count

a = [0,2,3,4,1,6,5]
print(min_swaps(a))
