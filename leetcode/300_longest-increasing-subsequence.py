from typing import *

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            max_ = 1
            tmp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp = dp[j] + 1
                if tmp > max_:
                    max_ = tmp
            dp[i] = max_
        return max(dp)

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
