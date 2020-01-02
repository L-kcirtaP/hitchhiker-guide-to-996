class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 0:
            return -1

        low, hi = 0, length - 1
        while low < hi:
            mid = int((low + hi) / 2)
            if nums[mid] > nums[hi]:
                low = mid + 1
            else:
                hi = mid

        pivot = low
        low, hi = 0, length - 1
        while low <= hi:
            mid = int((low + hi)/ 2)
            realmid = int((pivot + mid) % length)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                low = mid + 1
            else:
                hi = mid - 1

        return -1
