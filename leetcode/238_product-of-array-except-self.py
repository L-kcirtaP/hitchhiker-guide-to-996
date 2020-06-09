from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res

s = Solution()
res = s.productExceptSelf([1, 2, 3, 4])
print(res)
