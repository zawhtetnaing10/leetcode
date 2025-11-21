
dict = {
    "(": ")",
    "{": "}",
    "[": "]"
}


def isValid(s: str) -> bool:
    stack = []

    for char in s:
        if char in dict:
            stack.append(char)
        else:
            if stack and dict.get(stack[-1]) == char:
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(isValid("[({})]"))
