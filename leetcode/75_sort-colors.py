def sortColors(nums) -> None:
    red, white, blue = 0, 0, len(nums)-1
    while white <= blue:
        if nums[white] == 1:	# white
            white += 1
        elif nums[white] < 1:	# red
            nums[red], nums[white] = nums[white], nums[red]
            white +=1
            red += 1
        else:					# blue
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1           


nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
