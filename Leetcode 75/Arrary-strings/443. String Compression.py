class Solution:
    def compress(self, chars) -> int:
        length = len(chars)
        idx = 0
        i = 0
        while i < length:
            curr_char = chars[i]
            count = 0
            # Checking for duplicates
            while i< length and chars[i] == curr_char:
                count += 1
                i += 1
            # Assigning the duplicates count as strings to the array
            chars[idx] = curr_char
            idx += 1
            # if ['a', 'b'] we need to return only ['a', 'b'] and not ['a', '1', 'b','2']
            if count > 1:
                count_str = str(count)
                # For handling the case when count becomes more than one digit number.
                # '12' as '1', '2'
                for ch in count_str:
                    chars[idx] = ch
                    idx += 1
        return idx
    
a = Solution()
print(a.compress(["a","a","b","b","c","c","c"]))