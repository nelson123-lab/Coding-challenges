class Solution:
    
    def encode(self, strs):
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length
        return res

"""
- Here we first need to find a way to encode the strings. Adding a special in between the elements on the list doesn't work since these special characters can also be present in the string.
- We are using an encoding method in which the number of characters in each string is added as the first element followed by "#" followed by the string itself.
- In the decoding part we are using a while loop to check if the iteration is exceeding the string length or not first, then one while loop to extract the information of each string.
- The main idea is that the information for decoding can be present within the encrypted string.

Time Complexity O(n)
Space Complexity O(n)
"""
