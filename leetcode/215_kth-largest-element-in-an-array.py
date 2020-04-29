from typing import List

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return (heapq.heappop(nums))

s = Solution()
s.findKthLargest([1, 2, 3, 4, 5, 6, 1], 4)
