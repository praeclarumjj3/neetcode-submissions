class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1  # Empty t can always be formed once

        for char_s in s:
            # Go backward so this character from s is not reused
            for j in range(len(t), 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[len(t)]