class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        
        
        max_profit = 0

        left = -1
        right = 1
        profit = 0

        while left < right and left < len(prices) - 1:
            left += 1
            pl = prices[left]
            right = left + 1
            while right < len(prices):
                pr = prices[right]

                max_profit = max(max_profit,  pr-pl)

                right += 1
        return max_profit
                    
                





