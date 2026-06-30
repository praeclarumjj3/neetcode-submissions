class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        right = k

        if right == len(nums):
            return [max(nums)]
        
        l = []
        while right < len(nums)+1:
            l.append(max(nums[left:right]))
            left += 1
            right += 1

        return l
        