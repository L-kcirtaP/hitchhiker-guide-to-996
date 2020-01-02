class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sz = len(nums)
        for i in range(sz):
            for j in range(i+1, sz):
                if nums[i] + nums[j] == target:
                    return [i, j]
