def solution(nums):
    quick_sort(nums, 0, len(nums) - 1)

    return nums


def quick_sort(nums, low, high):
    if low < high:
        mid = partition(nums, low, high)
        quick_sort(nums, low, mid - 1)
        quick_sort(nums, mid + 1, high)


def partition(nums, low, high):
    i = low - 1
    pivot = nums[high]

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]

    nums[i + 1], nums[high] = nums[high], nums[i+1]

    return i + 1


print(f"{solution([4, 6, 7, 8, 1])}")
print(f"{solution([7, 0, 7, 8, 1, 2, 4, 3, 10, 12, 111])}")
