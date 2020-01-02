class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        p, length = 0, len(nums)
        if length < 3: return []
        
        three_sums = []
        while nums[p] <= 0 and p < length - 2:
            lp, rp = p + 1, length - 1
            # print("Before: p: {}, lp: {}, rp: {}".format(p, lp, rp))
            while lp < rp:
                s = nums[p] + nums[lp] + nums[rp]
                # print("Processing: p: {}, lp: {}, rp: {}".format(p, lp, rp))
                if s < 0:
                    lp += 1
                elif s > 0:
                    rp -= 1
                else:
                    three_sums.append([nums[p], nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp + 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp - 1]:
                        rp -= 1
                    lp += 1
                    rp -= 1

            # print("After: p: {}, lp: {}, rp: {}".format(p, lp, rp))
            while nums[p] == nums[p + 1]:
                if p >= length - 3: return three_sums
                p += 1
            p += 1

        return three_sums
