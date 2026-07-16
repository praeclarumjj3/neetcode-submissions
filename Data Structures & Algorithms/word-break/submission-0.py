class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # empty string can always be formed

        for end in range(1, len(s) + 1):
            for start in range(end):
                if dp[start] and s[start:end] in words:
                    dp[end] = True
                    break

        return dp[len(s)]