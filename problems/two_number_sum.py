def two_number_sum(nums, target):
    nums_hash = {}

    for num in nums:
        subtraction = target - num
        if subtraction in nums_hash:
            return [num, subtraction]
        else:
            nums_hash[num] = True

    return []


print(two_number_sum([2, 7, 11, 3, 5, 12, 8], target=18))
