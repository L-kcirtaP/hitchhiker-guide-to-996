class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        p, length = 0, len(nums)
        closest = 1024
        while p < length - 2:
            lp, rp = p + 1, length - 1
            while lp < rp:
                s = nums[p] + nums[lp] + nums[rp]
                val, closest_val = abs(target - s), abs(target - closest)
                if s < target:
                    if (val < closest_val): closest = s
                    lp += 1
                elif s > target:
                    if (val < closest_val): closest = s
                    rp -= 1
                else:
                    return target
            while nums[p] == nums[p + 1]:
                if p >= length - 3:
                    return closest
                p += 1
            p += 1
        return closest
