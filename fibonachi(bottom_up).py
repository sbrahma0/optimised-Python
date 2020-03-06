#Stair case problem(Fibonachi series),
def staircase(n):
    memo = [None] * (n+1)
    if n == 1:
        return 1
    if n == 2:
        return 2
        
    memo[1] = 1
    memo[2]  =2
    
    for l in range(3,n+1):
        memo[l] = memo[l-1]+memo[l-2]
    
    return memo[n]

print(staircase(6))
