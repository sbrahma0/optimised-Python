def getFirstDigit(x) : 
    while (x >= 10) : 
        x /= 10
    return x 
  
# method to return count of numbers with same 
# starting and ending digit from 1 upto x 
def getCountWithSameStartAndEndFrom1(x) : 
    if (x < 10): 
        return x 
  
    # get ten-spans from 1 to x 
    tens = x / 10
  
    # add 9 to consider all 1 digit numbers 
    res = tens + 9
  
    # Find first and last digits 
    firstDigit = getFirstDigit(x) 
    lastDigit = x % 10
  
    # If last digit is greater than first digit 
    # then decrease count by 1 
    if (lastDigit < firstDigit) : 
        res = res - 1
  
    return res 
  
# Method to return count of numbers with same starting 
# and ending digit between start and end 
def getCountWithSameStartAndEnd(start, end) : 
    return (getCountWithSameStartAndEndFrom1(end) - 
           getCountWithSameStartAndEndFrom1(start - 1)) 
  
# Driver Code 
start = 5
end = 40
print(getCountWithSameStartAndEnd(start, end)) 
