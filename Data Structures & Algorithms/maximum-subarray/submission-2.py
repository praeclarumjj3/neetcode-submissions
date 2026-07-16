class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        left = 0
        max_sum = min(nums)

        for left in range(len(nums)):
            right = left
            while right < len(nums):
                ms = sum(nums[left:right+1])
                if ms >= max_sum:
                    max_sum = ms
                right += 1
        
        return max_sum

        