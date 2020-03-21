# Array advanced game Non-greedy approach
# https://youtu.be/r7EzxgrYfNg?list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV

def array_advance_game(given_array):
    index = 0
    last_index = len(given_array)-1
    furthest_reached = 0
    # the second condition is like if the furthest_reached value already crosses the last index then it is winnable
    # the 1st condition is for the fact that if the furthest_reached is not updated by increasing positiions then it 
    #is possible that there has been zeros and thus if the comparing index becomes more than the maximum reaced index then it is no point
    while index <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, given_array[index]+index)
        index += 1
    
    return furthest_reached >= last_index # Since if the furthest_reached has value more than the last index it is certainly winnable


a = [3,3,1,0,2,0,1]
b = [3,2,0,0,2,0,1]



print(array_advance_game(b))
