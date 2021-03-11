import heapq
def fiveStarReviews(productRatings, threshold):
    heap = []
    total_percent = 0
    # this loop is to get the list which is gonna help us get most increase
    for rating, total in productRatings:
        percent = rating / total * 100
        new_percent = (rating + 1) / (total + 1) * 100
        increase = new_percent - percent
        heapq.heappush(heap, (-increase, rating, total))
        total_percent += percent
  
    ans = 0
    while (total_percent / len(productRatings) < threshold):
        increase, rating, total = heapq.heappop(heap)
        
        total_percent = total_percent + abs(increase)
        ans += 1
        
        rating += 1
        total += 1
        percent = rating / total * 100 # The current percent 
        next_percent = (rating + 1) / (total + 1) * 100
        increase = next_percent - percent
        heapq.heappush(heap, (-increase, rating, total))

    return ans
print(fiveStarReviews([[4,4],[1,2],[3,6]],77))
