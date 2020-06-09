class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bsearch(nums, start: int, end: int, target: int) -> int:
            if start == end:
                return start if nums[start] == target else -1

            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return bsearch(nums, middle+1, end, target)
            else:
                return bsearch(nums, start, middle, target)
    
    return bsearch(nums, 0, len(nums)-1, target)
