# qlink-https://algo.monster/problems/storage_optimization

def storage_optimization(n: int, m: int, h: List[int], v: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    cols = list(range(0,m+2))
    rows = list(range(0,n+2))
    for i in v:
        cols.remove(i)
    for j in h:
        rows.remove(j)
    
    width = 0
    for i in range(len(cols)-1):
        if cols[i+1]-cols[i] > width:
            width = cols[i+1]-cols[i]
    
    height = 0
    for i in range(len(rows)-1):
        if rows[i+1]-rows[i] > height:
            height = rows[i+1]-rows[i]
    
    return width*height
