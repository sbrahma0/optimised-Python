class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bst(array,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    t = node(array[mid])
    t.left = bst(array,start, mid-1)
    t.right = bst(array, mid+1, end)
    return t

a= [1,2,3,4,5,6,7,9]
a = bst(a,0, len(a)-1)
