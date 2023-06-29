class Solution:
    def compress(self, chars) -> int:
        length = len(chars)
        idx = 0
        i = 0
        while i < length:
            curr_char = chars[i]
            count = 0
            while i< length and chars[i] == curr_char:
                count += 1
                i += 1

            chars[idx] = curr_char
            idx += 1
            if count > 1:
                count_str = str(count)
                for ch in count_str:
                    chars[idx] = ch
                    idx += 1
        return idx
    
a = Solution()
print(a.compress(["a","a","b","b","c","c","c"]))