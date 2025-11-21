def selection_sort(nums):
    for i in range(len(nums)):

        smallest_idx = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j

        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]

    return nums


print(f"{selection_sort([4, 6, 7, 8, 1])}")
print(f"{selection_sort([7, 0, 7, 8, 1, 2, 4, 3, 10, 12, 111])}")
