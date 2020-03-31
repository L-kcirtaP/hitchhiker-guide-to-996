def maxProduct(nums) -> int:
	return max(maxProductCore(nums), maxProductCore(nums[::-1]))

def maxProductCore(nums) -> int:
	cur_max = max_so_far = nums[0]
	max_abs = 1 if nums[0] == 0 else nums[0]
	for i in nums[1:]:
		if i == 0:
			cur_max = i
			max_abs = 1
		else:
			max_abs = max_abs * i
			if max_abs > 0:
				cur_max = max_abs
			else:
				cur_max = max(cur_max, i)
			max_so_far = max(cur_max, max_so_far)
	return max_so_far

print(maxProduct([2,-5,-2,-4,3]))
