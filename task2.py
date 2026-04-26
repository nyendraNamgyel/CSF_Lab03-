def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return "Not Balanced"
            stack.pop()

    return "Balanced" if not stack else "Not Balanced"


expr1 = "(a+b)*(c+d)"
expr2 = "(a+b)*(c+d"

print(expr1, ":", is_balanced(expr1))
print(expr2, ":", is_balanced(expr2))