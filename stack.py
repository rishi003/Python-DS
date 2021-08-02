brackets = {
    '{': '}',
    '[': ']',
    '(': ')'
}

_brackets = {
    '}': '{',
    ']': '[',
    ')': '('
}


def balanced(str):
    stack = []
    for i in str:
        if i in brackets:
            stack.append(i)
        elif i in _brackets:
            if len(stack) > 0:
                s = stack.pop()
                if s != _brackets[i]:
                    return "unbalanced"
            else:
                return "unbalanced"

    return "balanced"


print(balanced("[()[{}]]"))
