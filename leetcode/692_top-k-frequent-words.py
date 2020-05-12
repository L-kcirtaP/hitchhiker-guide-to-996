from typing import *

class HeapNode:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        
    def __eq__(self, other):
        return self.freq == other.freq and self.val == other.val

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.val > other.val
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        occr = {}
        heap = []
        heapq.heapify(heap)
        for word in words:
            occr[word] = occr.get(word, 0) + 1

        for word, count in occr.items():
            heapq.heappush(heap, HeapNode(word, count))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(key=lambda x: (-x.freq, x.val))
        return [i.val for i in heap]


s = Solution()
# words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
# words = ["i", "love", "leetcode", "i", "love", "coding"]
words = ["aaa", "aa", "a"]
k = 2
print(s.topKFrequent(words, k))
