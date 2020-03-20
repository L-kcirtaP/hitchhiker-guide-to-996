def subsets(nums):
    result = []
    if not nums:
        return result

    _susbets(nums, 0, result)
    return result


def _susbets(nums, start, result):
    if start == len(nums)-1:
        result += [[], [nums[start]]]
    else:
        _susbets(nums, start+1, result)
        result += [[nums[start]]+x for x in result]


# def subsets(nums):
#     res = [[]]
#     for num in nums:
#         print(res)
#         res += [item+[num] for item in res]
#     return res

print(subsets([1, 2, 3]))
