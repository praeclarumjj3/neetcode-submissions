from bisect import bisect_left
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones.sort()

        if len(stones) == 1:
            return stones.pop()

        stone = stones.pop()
        
        while len(stones):
            s = stones.pop()
            stone = abs(stone-s)
            if len(stones) == 0:
                return stone
            idx = bisect_left(stones, stone)
            stones = stones[:idx] + [stone] + stones[idx:]
            stone = stones.pop()

        return stone