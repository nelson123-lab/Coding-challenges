"""
The main thing to note here is that we are not allowed to use extra space to store the compressed string as per the description so our algorithm should work in O(n) space Complexity.
- If we could have returned the compressed string separately it is an easy problem. We can do this in the below way.
"""
class Solution:
    def compress(self, chars) -> int:
        ref = {}
        res = ""
        for i in range(len(chars)):
            if chars[i] not in ref:
                ref[chars[i]] = 1
            else:
                ref[chars[i]] = ref[chars[i]] + 1
        
        for key, value in ref.items():
            res = res + key + str(value)

        return len(res), res
a = Solution()
print(a.compress(["a","a","b","b","c","c","c"]))

# Output 
#(6, 'a2b2c3')

"""
The above solution is not accepted. Thus we need to edit the values of the input list within itself.
"""
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

""""
Time Compelxity O(n)
Space Complexity O(1)
"""
