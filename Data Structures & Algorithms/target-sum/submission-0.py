class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total:
            return 0

        offset = total
        dp = [0] * (2 * total + 1)

        # Sum 0 is stored at index offset.
        dp[offset] = 1

        for n in nums:
            next_dp = [0] * (2 * total + 1)

            for current_sum in range(-total, total + 1):
                current_idx = current_sum + offset

                if dp[current_idx] == 0:
                    continue

                plus_idx = current_sum + n + offset
                minus_idx = current_sum - n + offset

                next_dp[plus_idx] += dp[current_idx]
                next_dp[minus_idx] += dp[current_idx]

            dp = next_dp

        return dp[target + offset]