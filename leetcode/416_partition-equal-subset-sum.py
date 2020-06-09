class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2:
            return False
        target = sum_ / 2

        knapsack = [[0]*len(nums) for _ in range(target)]
        for i in range(len(nums)):
            knapsack[i][target] = 0
        
        for i in range(len(nums))
        
        return True

