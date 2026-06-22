class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        entries = {}
        for x in nums:
            if x in entries:
                return True
            else:
                entries[x] = 1
        return False
        