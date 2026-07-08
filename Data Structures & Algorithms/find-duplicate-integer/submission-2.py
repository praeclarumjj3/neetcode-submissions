class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        prev = sorted_nums[0]
        for n in sorted_nums[1:]:
            if n == prev:
                return n
            prev = n
        