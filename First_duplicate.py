def printRepeating(arr): 
    
    size = len(arr)
    #print("The repeating elements are: ") 
      
    for i in range(0, size): 
          
        if arr[abs(arr[i])-1] >= 0: 
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1] 
        else: 
            print('The first number to appear as duplicate is ',arr[i]) 
            break
    
    
              
# Driver code 
arr = [1,2,3,2,3,4,5] 
printRepeating(arr) 
