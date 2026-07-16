class Solution:
    def rob(self, nums: List[int]) -> int:

        dp1 = [0] * (len(nums)-1) # skip last
        dp2 = [0] * (len(nums)-1) # skip 0

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp1[0] = nums[0]
        dp2[0] = nums[1]
        dp1[1] = max(nums[1], dp1[0])
        dp2[1] = max(nums[2], dp2[0])
        
        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1])
        
        return max(dp2[-1], dp1[-1])

