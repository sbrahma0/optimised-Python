#This has a high time complexity
import itertools

def max_multiple_of_3(l):
    '#remove the zeros to speed combinatorial analysis:'
    for i in range(l.count(0)):
        l.pop(l.index(0))
        
    b = len(l)
    l = sorted(l, reverse = True)
    while b > 0:
        combo = itertools.combinations(l, b) # This creates all possible subsets from the main list
        for thing in combo:


            if sum(thing) % 3 == 0:
                
                max_div_3 = ''
                for digit in thing:
                    max_div_3 += str(digit)
                return int(max_div_3)
        b -= 1

    return 0

arr = [2,7]
print(max_multiple_of_3(arr))
