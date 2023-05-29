def validPalindrome(s: str) -> bool:
    a, b = s[:-1], s[1:]
    if s[::-1] == s:
        return True
    elif a[::-1] == a or b[::-1] == b:
        return True
    else:
        for i in range(1, len(s[1:-1])+1):
            left, right = i, len(s)-i-1
            new_char = ""
            # convert string to list
            s_list = list(s)

            # replace character at index
            s_list[left] = new_char

            # convert list back to string
            new_s = "".join(s_list)
            if new_s[::-1] == new_s:
                return True
            s_list = list(s)
            s_list[right] = new_char
            new_s = "".join(s_list)
            if new_s[::-1] == new_s:
                return True
        return False

print(validPalindrome("eddze"))