def majorityElement(nums) -> int:
    occ = {}
    size = len(nums)
    for i in nums:
        occ[i] = occ.get(i, 0) + 1

    return [k for k, v in occ.items() if v > size//3]

print(majorityElement([1,1,1,3,3,2,2,2]))