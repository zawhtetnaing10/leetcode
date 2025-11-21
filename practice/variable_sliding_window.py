def longest_distince_characters(s, k):
    first_idx = 0
    second_idx = 0

    char_map = {}
    max_length = 0

    while second_idx < len(s) - 1:
        # expand the window
        second_idx += 1
        # add the new character to the map
        new_char = s[second_idx]
        if new_char in char_map:
            char_map[new_char] += 1
        else:
            char_map[new_char] = 1

        # If no. of distinct chars more than k, shrink the window
        if len(char_map) > k:

            # shrink the window
            first_idx += 1

            # Remove the char or decrease the count
            char_to_be_removed = s[first_idx]
            char_map[char_to_be_removed] -= 1
            if char_map[char_to_be_removed] == 0:
                del char_map[char_to_be_removed]

        # Using first_idx and second_idx, find the new length and update max_length
        new_length = second_idx - first_idx + 1

        max_length = max(max_length, new_length)

    return max_length


print(longest_distince_characters("eceba", 2))
print(longest_distince_characters("aaabbc", 2))
print(longest_distince_characters("loveleetcode", 4))
