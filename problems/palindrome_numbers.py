def palindrome_num(num: int):
    if num < 0:
        return False
    return str(num) == str(num)[::-1]


print(palindrome_num(121))
print(palindrome_num(-121))
print(palindrome_num(343))
