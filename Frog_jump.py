A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.


from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stonesofstones = set(stones) # traversing a set happens faster than list
        
        @lru_cache(None)
        def canJump(stonePos, jumpUnits):
            if jumpUnits<=0 or stonePos not in stonesofstones:
                return False
            if stonePos == target:
                return True
            
            return canJump(stonePos+jumpUnits, jumpUnits) or canJump(stonePos+jumpUnits+1, jumpUnits+1) or canJump(stonePos+jumpUnits-1, jumpUnits-1)
        return canJump(1,1)
