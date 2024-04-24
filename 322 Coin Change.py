class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 0
        

        dp = [float('inf')] * (amount + 1)
        dp[-1] = float('inf')

        coins = sorted(coins)

        for i in coins:
            if i < len(dp):
                dp[i] = 1

        for i in range(len(dp)):
            for coin_val in reversed(coins):
                if ((i-coin_val >= 0) and dp[i-coin_val] != float('inf') and dp[i-coin_val] + 1 < dp[i]):
                    dp[i] = dp[i-coin_val] + 1
        
        if dp[-1] == float('inf'):
            return -1

        return dp[-1]

obj = Solution()
print(obj.coinChange([1,2,5], 11))
print(obj.coinChange([2], 3))
print(obj.coinChange([1], 0))