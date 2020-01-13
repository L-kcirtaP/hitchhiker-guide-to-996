from typing import List
import json

class Solution:
    def _findMedianSingleArray(self, nums: List[int]) -> float:
        sz = len(nums)
        if sz % 2 == 0:
            return (nums[sz/2-1] + num[sz/2]) / 2
        else:
            return nums[sz/2-1]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return _findMedianSingleArray(nums2)
        if not nums2:
            return _findMedianSingleArray(nums1)

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);
            
            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
