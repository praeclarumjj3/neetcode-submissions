class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        # We do not need to jump from the final index.
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # We have finished examining every position
            # reachable with the current number of jumps.
            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    break

        return jumps