class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtrack(perm):
            if len(perm) == len(nums):
                permutations.append([nums[i] for i in perm])
                return
            
            for i in range(len(nums)):
                if i in perm:
                    continue
                perm.append(i)
                backtrack(perm)
                perm.pop()
        
        backtrack([])
        return permutations
            
        