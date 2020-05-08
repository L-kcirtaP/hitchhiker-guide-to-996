from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc = 0
        for i in nums:
        	acc = acc ^ i
        return acc


s = Solution()
print(s.singleNumber([4,1,2,1,2]))