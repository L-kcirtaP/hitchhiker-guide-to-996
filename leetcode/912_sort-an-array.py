def partition(nums, start, end):
    pivot = nums[start]
    p1, p2 = start+1, end
    while p1 <= p2:
        if nums[p1] <= pivot:
            p1 += 1
        if nums[p2] > pivot:
            p2 -= 1
        if p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]

    nums[start], nums[p2] = nums[p2], nums[start]
    return p2


def quickSort(nums):
    def quickSortCore(nums, start, end):
        if start >= end:
            return
        p = partition(nums, start, end)
        quickSortCore(nums, start, p-1)
        quickSortCore(nums, p+1, end)

    quickSortCore(nums, 0, len(nums)-1)

nums = [5, 1, 4, 7, 2, 7, 3, 2, 5]
quickSort(nums)
print(nums)
