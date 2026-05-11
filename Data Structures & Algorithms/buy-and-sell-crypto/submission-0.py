class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)):
            l=0
            while l<i:
                if i>0 and prices[l]<prices[i]:
                    if profit<prices[i]-prices[l]:
                        profit=prices[i]-prices[l]
                l+=1
        return profit
                



        