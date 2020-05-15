from typing import *

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return

        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        foo = 0
        while foo != slow:
            foo = nums[foo]
            slow = nums[slow]

        return slow

s = Solution()
print(s.findDuplicate([3,1,3,4,2]))
