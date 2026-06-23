class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_n = len(nums)

        ans = [1] * len_n

        prefix = 1

        for idx, n in enumerate(nums):
            ans[idx] = prefix
            prefix *= n

        suffix = 1
        for idx, n in enumerate(nums[::-1]):
            ans[len_n - 1- idx] *= suffix
            suffix *= n
        
        return ans
        