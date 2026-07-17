class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)

        # dp[j] means:
        # s1[:i] and s2[:j] can form s3[:i+j]
        dp = [False] * (n + 1)
        dp[0] = True

        # Use only characters from s2
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # Use only characters from s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                target_char = s3[i + j - 1]

                take_from_s1 = (
                    dp[j] and s1[i - 1] == target_char
                )

                take_from_s2 = (
                    dp[j - 1] and s2[j - 1] == target_char
                )

                dp[j] = take_from_s1 or take_from_s2

        return dp[n]