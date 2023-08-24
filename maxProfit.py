class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit
    
#Example

solution = Solution()
prices = [9, 4, 8, 6, 7]
ans = solution.maxProfit(prices)
print(ans)