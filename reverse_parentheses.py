def reverseParentheses(s: str) -> str:
    stack = []
    chars = list(s)
    
    for i in range(len(chars)):
        if chars[i] == '(':
            stack.append(i)
        elif chars[i] == ')':
            j = stack.pop()
            chars[j:i] = chars[j:i][::-1]
    
    return ''.join(c for c in chars if c not in '()')
