def maxSubArray(nums) -> int:
	cur_max = max_so_far = nums[0]
	for i in nums[1:]:
		cur_max = max(i, cur_max+i)
		max_so_far = max(cur_max, max_so_far)
	return max_so_far

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))