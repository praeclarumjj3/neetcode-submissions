class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(start, combo, total):
            if total == target:
                combinations.append(combo.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                combo.append(nums[i])

                # i, not i + 1, because nums[i] can be reused
                backtrack(i, combo, total + nums[i])

                combo.pop()

        backtrack(0, [], 0)
        return combinations