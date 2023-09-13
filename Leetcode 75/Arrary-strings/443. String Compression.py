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
        len_chars = len(chars)
        if not chars:
            return 0
        if len_chars == 0 or len_chars == 1:
            return len_chars
        
        idx = 0 # Index for the modification of the array
        i = 0 # Index for iteration of the array
        

        while i < len_chars:
            count = 0
            curr = chars[i]
            # Checking for duplicates
            while i < len_chars and chars[i] == curr:
                count += 1
                i += 1
            # Assigning the duplicates count as strings to the array
            chars[idx] = curr
            idx += 1
            # if ['a', 'b'] we need to return only ['a', 'b'] and not ['a', '1', 'b','2']
            if count > 1:
                # For handling the case when count becomes more than one digit number.
                # '12' as '1', '2'
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1
        return idx
    
a = Solution()
print(a.compress(["a","a","b","b","c","c","c"]))

""""
Time Compelxity O(n)
- There is only one iteration happening through the entire array.
Space Complexity O(1)
- No additional space is used here.
"""
