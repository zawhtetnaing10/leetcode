def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i

        while j >= 1 and nums[j] < nums[j-1]:
            nums[j-1], nums[j] = nums[j], nums[j - 1]
            j -= 1

    return nums


print(f"{insertion_sort([4, 6, 7, 8, 1])}")
print(f"{insertion_sort([7, 0, 7, 8, 1, 2, 4, 3, 10, 12, 111])}")
