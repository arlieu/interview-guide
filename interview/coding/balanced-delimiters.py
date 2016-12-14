'''Determine if a string contains balanced delimiters.'''
def balanced(s):
    stack = []
    for i in s:
        if i == '{' or i == '[' or i == '(':
            stack.append(i)

        elif i == '}':
            if not stack or stack.pop() != '{':
                return False

            continue

        elif i == ']':
            if not stack or stack.pop() != '[':
                return False

            continue

        elif i == ')':
            if not stack or stack.pop() != '(':
                return False

            continue

    if stack:
        return False

    return True