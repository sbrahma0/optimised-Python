'''
https://aonecode.com/amazon-online-assessment-cutoff-ranks
'''

def countLevelUpPlayers(cutOffRank, num, scores):
    count={}
    if num>=100000:
      return
    for score in sorted(scores,reverse=True):
        if score in count:
            count[score] += 1
        else:
            count[score] = 1
    
    ans, current = 0,1
    for i in count:
        if current>cutOffRank:
            break
        current += count[i]
        ans += count[i]
    return ans

print(countLevelUpPlayers(4,5,[2,2,3,4,5]))
