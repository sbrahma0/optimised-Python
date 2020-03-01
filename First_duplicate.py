'''
starts with 0 index, gets the element of that index then (that number-1) index element is checked whether it is -ve, if it 
is not then make it -ve else the previous index i.e., the index in the current loop is the answer
https://youtu.be/XSdr_O-XVRQ
'''
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
