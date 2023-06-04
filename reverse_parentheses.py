def reverseParentheses(s: str) -> str:
    # Using a stack to store the index of the Starting parentheses '('
    stack = []
    # Converting the string to a list to list operations.
    chars = list(s)
    
    for i in range(len(chars)):
        if chars[i] == '(':
            # Appending the index of starting parentheses '(' to the stack
            stack.append(i)
        elif chars[i] == ')':
            # Storing the value of the inner most starting parentheses index to j.
            j = stack.pop()
            # Reversing the elements betweent the index from '(' to ')'.
            chars[j:i] = chars[j:i][::-1]
    
    return ''.join(c for c in chars if c not in '()')

print(reverseParentheses("(u(love)i)"))
