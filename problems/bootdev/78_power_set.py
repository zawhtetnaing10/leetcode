def power_set(nums: list[int]) -> list[list[int]]:
    if not nums:
        return [[]]

    all_subsets = [[]]

    for element in nums:
        new_subsets = []
        for subset in all_subsets:
            new_subset = subset + [element]
            new_subsets.append(new_subset)

        all_subsets.extend(new_subsets)

    return all_subsets


print(f"{power_set([1, 2])}")
print(f"{power_set([1, 2, 3])}")
