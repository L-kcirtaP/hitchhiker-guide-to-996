class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
        	index = num - 1
        	nums[index] = -abs(nums[index])

        return [i for i in nums if i > 0]