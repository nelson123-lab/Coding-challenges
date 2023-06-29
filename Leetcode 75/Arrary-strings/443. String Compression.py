class Solution:
    def compress(self, chars) -> int:
        count = 1
        initial = chars[0]
        idx = 1
        chars1 = chars.copy()
        for i, e in enumerate(chars, 1):
            if e == initial:
                count += 1
                chars1[idx] = count
            else:
                count = 1
                idx = i+1
        return chars
    
a = Solution()
print(a.compress(["a","a","b","b","c","c","c"]))