class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        if len(s) == 1:
            return 1

        dp = [0] * len(s)
        dp[0] = 1

        # Decode s[1] alone
        if s[1] != "0":
            dp[1] += dp[0]

        # Decode s[0:2] together
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1

        for i in range(2, len(s)):
            # Use s[i] as a single-digit letter
            if s[i] != "0":
                dp[i] += dp[i - 1]

            # Use s[i - 1] and s[i] as a two-digit letter
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]