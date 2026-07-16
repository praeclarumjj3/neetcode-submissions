class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i] = [hold, sold, rest]
        dp = [[0, 0, 0] for _ in range(n)]

        dp[0][0] = -prices[0]  # bought on day 0
        dp[0][1] = 0           # cannot sell yet
        dp[0][2] = 0           # do nothing

        for i in range(1, n):
            # Either keep holding, or buy today after resting yesterday
            dp[i][0] = max(
                dp[i - 1][0],
                dp[i - 1][2] - prices[i]
            )

            # To sell today, we must have held yesterday
            dp[i][1] = dp[i - 1][0] + prices[i]

            # Rest today: either rested yesterday or sold yesterday
            dp[i][2] = max(
                dp[i - 1][2],
                dp[i - 1][1]
            )

        return max(dp[-1][1], dp[-1][2])