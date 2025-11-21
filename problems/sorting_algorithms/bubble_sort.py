def bubble_sort(nums):
    swapping = True

    end = len(nums)

    while swapping:
        swapping = False

        for i in range(1, end):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                swapping = True

        end -= 1

    return nums


print(f"{bubble_sort([4, 6, 7, 8, 1])}")
print(f"{bubble_sort([7, 0, 7, 8, 1, 2, 4, 3, 10, 12, 111])}")
