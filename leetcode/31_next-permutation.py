from typing import List
import json

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            pass

        else:
            
            print(3124)


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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
            nums = stringToIntegerList(line);
            
            ret = Solution().nextPermutation(nums)

            out = integerListToString(nums)
            if ret is not None:
                print("Do not return anything, modify nums in-place instead.")
            else:
                print(out)

        except StopIteration:
            break

if __name__ == '__main__':
    main()
