class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0
        l, r = 0, 0
        while r < len(prices):
            if prices[l]>prices[r]:
                l = r
                r+=1
            else:
                profit = prices[r]-prices[l]
                most = max(most, profit)
                r+=1
        return most