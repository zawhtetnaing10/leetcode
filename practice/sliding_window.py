def find_max_sum_of_contiguous_sub_array(nums, count):
    first_idx = 0
    second_idx = count - 1

    # Find the initial sum
    max_sum = 0
    for i in range(0, second_idx + 1):
        max_sum += nums[i]

    print(max_sum)

    # Apply sliding window
    while second_idx < len(nums) - 1:
        new_sum = max_sum
        new_sum -= nums[first_idx]
        first_idx += 1

        second_idx += 1
        new_sum += nums[second_idx]

        max_sum = max(max_sum, new_sum)

    return max_sum


print(find_max_sum_of_contiguous_sub_array([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))
print(find_max_sum_of_contiguous_sub_array([1, 5, 2, 9, 1], 2))
print(find_max_sum_of_contiguous_sub_array([-1, -3, -5, -2, -4], 3))
