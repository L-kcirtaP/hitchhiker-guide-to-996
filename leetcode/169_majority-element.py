def majorityElement(nums) -> int:
    occ = {}
    size = len(nums)
    for i in nums:
        occ[i] = occ.get(i, 0) + 1
        if occ[i] > size // 2:
            return i


## better solution with O(1) space
def majorityElementBetter(nums) -> int:
	top = -1
	cnt = 0
	for num in nums:
		if cnt == 0:
			top = num
			cnt += 1
		else:
			if num == top:
				cnt += 1
			else:
				cnt -= 1
	return top

