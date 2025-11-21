def palindrome(s):
    if len(s) == 0:
        return True

    # Remove non-alphanumeric
    chars = []
    for char in s:
        if char.isalnum():
            chars.append(char)

    # Check if palindrome
    left, right = 0, len(chars) - 1

    while left <= right:
        if chars[left].lower() != chars[right].lower():
            return False

        left += 1
        right -= 1

    return True

# O(N) Time and O(N) Space


print(palindrome("A man, a plan, a canal: Panama"))
print(palindrome("race a car"))
print(palindrome("Racecar"))
print(palindrome("Mom"))
