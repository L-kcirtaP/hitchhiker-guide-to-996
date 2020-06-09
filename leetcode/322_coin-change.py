from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INVALID = 10000
        dp = [[INVALID] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 0

        for j in range(1, amount+1):
            for coin in range(len(coins)):
                if j - coins[i] >= 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-coins[i]]+1)
        res = [dp[i][-1] for i in range(len(coins))]
        return min(res) if min(res) != INVALID else -1

s = Solution()
print(s.coinChange([1,2147483647], 2))
