def removeDuplicatesFromSortedArray(nums):
    first_idx = 0
    second_idx = 1

    while (second_idx < len(nums)):
        first_num = nums[first_idx]
        second_num = nums[second_idx]

        if first_num == second_num:
            second_idx += 1
        else:
            first_idx += 1
            nums[first_idx] = nums[second_idx]
            second_idx += 1

    return first_idx + 1, nums


print(removeDuplicatesFromSortedArray([1, 1, 1, 2, 2, 2, 3, 4, 4, 5]))
print(removeDuplicatesFromSortedArray([0, 0, 0, 6, 7, 7, 7, 19, 19, 20, 21]))
