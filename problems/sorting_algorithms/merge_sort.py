def merge_sort(nums):

    if len(nums) < 2:
        return nums

    mid_idx = len(nums) // 2

    first = merge_sort(nums[:mid_idx])
    second = merge_sort(nums[mid_idx:])

    return merge(first, second)


def merge(first, second):
    i = 0
    j = 0

    result = []

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    if i < len(first):
        result.extend(first[i:])

    if j < len(second):
        result.extend(second[j:])

    return result


print(f"{merge_sort([4, 6, 7, 8, 1])}")
print(f"{merge_sort([7, 0, 7, 8, 1, 2, 4, 3, 10, 12, 111])}")
