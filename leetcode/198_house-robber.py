from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sz = len(nums)
        if sz == 1:
            return nums[0]

        dp = [0] * sz
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[sz-1]

s = Solution()
res = s.rob([2,7,9,3,1])
print(res)