def two_pointers(numbers, target):

    numbers.sort()

    first_index = 0
    last_index = len(numbers) - 1

    while (first_index <= last_index):
        first_num = numbers[first_index]
        second_num = numbers[last_index]

        sum = first_num + second_num

        if sum == target:
            return [first_num, second_num]
        elif sum < target:
            first_index += 1
        elif sum > target:
            last_index -= 1


print(two_pointers([2, 7, 11, 3, 5, 12, 8], target=18))
