class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Convert word1[i:] into an empty string: delete everything
        for i in range(m + 1):
            dp[i][n] = m - i

        # Convert an empty string into word2[j:]: insert everything
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = dp[i][j + 1]
                    delete = dp[i + 1][j]
                    replace = dp[i + 1][j + 1]

                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[0][0]