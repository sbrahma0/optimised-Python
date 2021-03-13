# qlink - https://algo.monster/problems/amazon_oa_find_all_combination_of_numbers_sum_to_target

def number_of_options(prices_of_jeans: List[int], prices_of_shoes: List[int], prices_of_skirts: List[int], prices_of_tops: List[int], budget: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    items = [prices_of_jeans, prices_of_shoes, prices_of_skirts, prices_of_tops]

    global res 
    res = 0

    def backtrack(items, start, rem):
        global res

        if start == len(items):
            if rem >= 0:  res += 1
            return
        
        for i in range(len(items[start])):
            backtrack(items, start + 1, rem - items[start][i])
    
    backtrack(items, 0, budget)
    return res
