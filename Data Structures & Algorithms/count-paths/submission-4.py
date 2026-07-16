class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # From any cell in the last column, there is only one path:
        # keep moving down.
        for i in range(m):
            dp[i][n - 1] = 1

        # From any cell in the last row, there is only one path:
        # keep moving right.
        for j in range(n):
            dp[m - 1][j] = 1

        # Fill from bottom-right toward top-left.
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]