'''
You are given a list of meeting durations, give the numer of meeting rooms required
'''


import heapq

def meeting_room(arr):
    
    arr.sort()
    
    rooms = 1
    heap = [arr[0][1]]
    
    for start, end in arr[1:]:
        if start< heap[0]:
            heapq.heappush(heap, end)
            #print(heap)
            #print(start, end)
            rooms = max(rooms, len(heap))
        else:
            heapq.heappop(heap)
    
    return rooms

arr = [[0,30],[5,10],[10,20],[20,30],[30,50]]
print(meeting_room(arr))
    
