def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


print(f"{removeDuplicates("abbaca")}")
print(f"{removeDuplicates("zbbaazcddcn")}")
