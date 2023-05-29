def validPalindrome(self, s: str) -> bool:
    if s[::-1] == s:
        return True
    elif s[:-1][::-1] == s[:-1] or s[1:][::-1] == s[1:]:
        return True
    else:
        for i in s[1:-1]:
            c = s.replace(i,"")
            if c[::-1] == c:
                return True
            else:
                pass
        return False

print(validPalindrome("pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"))