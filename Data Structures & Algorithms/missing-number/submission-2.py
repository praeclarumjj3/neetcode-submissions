class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp_sum = len(nums) * (len(nums) + 1) // 2

        giv_sum = 0
        for n in nums:
            giv_sum += n
        
        return exp_sum - giv_sum
        