# Printing a Matrix in spiral form

def spiralPrint(m,n,a): # n-col, m-row
    k = 0
    l = 0
    
    while k<m and l<n:
        # From left to right
        for i in range (l,n):
            print(a[k][i], end="")
        k += 1
        
        #print('*******')
        # From top to bottom
        #print("-------",k,m,l,n)
        for i in range (k, m):
            print(a[i][n-1], end="")
        n -= 1
        
        #print("*******")
        # Right to left
        if k<m:
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end="")
            m -= 1
        #print("-------",k,m,l,n)
        #print("**********")
        # Bottom to top
        
        if l<n:
            for i in range(m-1,k-1,-1):
                print(a[i][l], end="")
            l += 1
        #print("-------",k,m,l,n)
        #break
    
# Drivers code
a = [ [1, 2, 3, 4], 
      [7, 8, 9, 10], 
      [13, 14, 15, 16] ,[17, 18, 19, 20]] 
        
R = 4; C = 4
spiralPrint(R, C, a) 




