def palindrome(text):

    first_idx = 0
    second_idx = len(text) - 1

    while first_idx <= second_idx:
        if text[first_idx] != text[second_idx]:
            return False

        first_idx += 1
        second_idx -= 1

    return True


print(palindrome("racecar"))
print(palindrome("mom"))
print(palindrome("madam"))
print(palindrome("caelid"))
