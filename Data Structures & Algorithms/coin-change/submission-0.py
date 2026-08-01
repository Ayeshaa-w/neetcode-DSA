class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)#initialisation of array calld dp that holds max no.of coins required
        dp[0]=0 #amount=0 0 coins required
        for amounts in range(1,amount+1):
            for coin in coins:
                if amounts-coin>=0:
                    dp[amounts]=min(dp[amounts],1+dp[amounts-coin])
        return dp[amount] if dp[amount]!=amount+1 else -1


        