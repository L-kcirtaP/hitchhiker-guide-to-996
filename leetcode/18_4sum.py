class Solution:
    def threeSum(self, nums: list, target: int) -> list:
        nums.sort()
        p, length = 0, len(nums)
        if length < 3:
            return []
        three_sums = []
        while p < length - 2:
            lp, rp = p + 1, length - 1
            while lp < rp:
                s = nums[p] + nums[lp] + nums[rp]
                if s < target:
                    lp += 1
                elif s > target:
                    rp -= 1
                else:
                    three_sums.append([nums[p], nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp - 1]:
                        rp -= 1
                    lp += 1
                    rp -= 1
            while p < length - 3 and nums[p] == nums[p + 1]:
                p += 1
            p += 1
        return three_sums

    def fourSum(self, nums: list, target: int) -> list:
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        four_sums = []
        start = 0
        while start < length - 3:
            three_sums = self.threeSum(nums[start + 1:], target - nums[start])
            for three_sum in three_sums:
                four_sums.append([nums[start]] + three_sum)
            while start < length - 3 and nums[start] == nums[start + 1]:
                start += 1
            start += 1
        return four_sums
