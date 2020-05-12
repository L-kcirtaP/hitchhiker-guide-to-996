from typing import *

class HeapNode:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        
    def __eq__(self, other):
        return self.freq == other.freq

    def __gt__(self, other):
        return self.freq > other.freq
    
    def __lt__(self, other):
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        occr = {}
        heap = []
        heapq.heapify(heap)
        for num in nums:
            occr[num] = occr.get(num, 0) + 1
            flg = False
            for i in heap:
                if i.val == num:
                    flg = True
                    break

            if flg:
                i.freq += 1
            else:
                if len(heap) < k:
                    heapq.heappush(heap, HeapNode(num, occr[num]))
                elif occr[num] > heap[0].freq:
                    heapq.heappop(heap)
                    heapq.heappush(heap, HeapNode(num, occr[num]))
                heapq.heapify(heap)

        return [i.val for i in heap]


nums = [5,2,5,3,5,3,1,1,3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))