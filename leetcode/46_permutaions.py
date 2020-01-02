class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        perms = []
        for i, num in enumerate(nums):
            nums_cp = nums[:]
            nums_cp.pop(i)
            perms += list(map(lambda x: [num] + x, self.permute(nums_cp)))
        return perms
