def print_mat_spiral(a,i,j,R,C):
    if (i>R-1) or (j>C-1):
        print("\n END")
        return
    # First row
    for p in range(j,C):
        print(a[i][p],end=" ")
    # Last column
    for p in range(i+1,R):
        print(a[p][C-1],end=" ")
    
    # Last Row
    if (R-1 != i):
        for p in range(C-2,j-1,-1):
            print(a[R-1][p],end=" ")
    
    # Fist column
    if (C-1 != j):
        for p in range(R-2,i,-1):
            print(a[p][j],end=" ")
    
    print_mat_spiral(a, i+1, j+1, R-1, C-1)

a = [[1, 2, 3, 4],[12, 13, 14, 5],[11, 16, 15, 6]]
print_mat_spiral(a,0,0,len(a),len(a[0])) # MAtrix, i,j,R,C
