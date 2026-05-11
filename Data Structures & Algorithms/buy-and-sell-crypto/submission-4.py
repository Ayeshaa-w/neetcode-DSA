class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        maxProfit = 0
        i = 1
        n = len(prices)
        while( i < n):
            min_ = min(min_, prices[i])
            diff = prices[i] - min_
            maxProfit = max( maxProfit, diff)
            i += 1
        return maxProfit






            

        