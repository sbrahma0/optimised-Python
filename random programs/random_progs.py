'''
# Flip 0 to 1 if any of its adjacent neighbours(not diagonals) is 1.

mat = [[1, 0, 1, 0],[0, 0, 1, 0],[0, 0, 0, 0]] 

def flip(mat):
    r = len(mat)
    c = len(mat[0])
    neigh = []
    count = 0
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 1:
                if (i+1,j) not in neigh:
                    neigh.extend([(i+1,j)])
                if (i-1,j) not in neigh:
                    neigh.extend([(i-1,j)])
                if (i,j+1) not in neigh:
                    neigh.extend([(i,j+1)])
                if (i,j-1) not in neigh:
                    neigh.extend([(i,j-1)])
    for i in range(r):
        for j in range(c):
            if (i,j) in neigh and mat[i][j]==0:
                count += 1
                mat[i][j] = 1
    return mat, count
    

print(flip(mat))
'''
'''
# Find the continuous subset which gives the required sum from an unsirted array
def cont(array, s):
    i, j, su = 0,0,0
    
    while i<len(array) and j<len(array):
        su += array[j]
        if su==s:
            if i!=j:
                return i,j
            else:
                return i
        
        if su < s:
            j += 1
        
        if su > s:
            su -= array[i]
            i += 1
            j += 1
        
    
    return

array = [7,8,3,2,1,5,4]
print(cont(array, 24))
'''
