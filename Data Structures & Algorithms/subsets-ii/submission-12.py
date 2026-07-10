class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        subsets = []

        def backtrack(sub, idx):
            subsets.append(sub.copy())
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                sub.append(nums[i])
                backtrack(sub, i+1)
                sub.pop()
            
        backtrack([], 0)
        return subsets
        