'''
This function is to get the total number of counts for each character in the string
'''
def get_char_counts(string):
    no_of_chars = 256
    count = [0]*no_of_chars
    
    
    for i in string:
        count[ord(i)]+=1
    #print(count)
    return count
  
def first_non_repeating(string):
    count = get_char_counts(string)
    first_non_repeating_index = -1
    l = 0
    
    for i in string:
        if count[ord(i)] == 1:
            first_non_repeating_index = l
            break
        l = l+1
    
    return first_non_repeating_index

# Driver 
string = "sasd"
index = first_non_repeating(string) 
if index==-1: 
    print ("Either all characters are repeating or string is empty")
else: 
    print ("First non-repeating character is " + string[index])
