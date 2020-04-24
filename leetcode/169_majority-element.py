def majorityElement(nums) -> int:
    occ = {}
    size = len(nums)
    for i in nums:
        occ[i] = occ.get(i, 0) + 1
        if occ[i] > size // 2:
            return i
