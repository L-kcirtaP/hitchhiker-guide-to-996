from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        i = len(nums) - 2
        while i >= 0 and nums[i] > nums[i+1]:
            i -= 1
        if i < 0:
            nums.reverse()
            return
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

        x, y = i+1, len(nums)-1
        while x < y:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1; y -= 1

s = Solution()
nums = [1, 2, 3]
s.nextPermutation(nums)
print(nums)
s.nextPermutation(nums)
print(nums)
s.nextPermutation(nums)
print(nums)
s.nextPermutation(nums)
print(nums)
s.nextPermutation(nums)
print(nums)
s.nextPermutation(nums)
print(nums)
