class Solution(object):
    def longestCommonPrefix(self, strs):
        # Checking whether the strs contain elements
        if not strs:
            return ""
        # Choosing the prefix as the first word.
        prefix = strs[0]
        for i in range(1, len(strs)):
            # Checking whether the predix exists starting from the first index.
            while strs[i].find(prefix) != 0:
                # removing the last element.
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    """
    The in function cannot be used here which will result in prefix in some parts of the strings. 
    - The .find() function in Python is a built-in string method that returns the index of the first occurrence of a substring in a string. 
    If the substring is not found, it returns -1.


    - To find the longest common prefix among an array of strings, we can start by comparing the first character of all the strings. If they are the same, we 
    move on to the next character and continue the comparison. If at any point the characters are not the same, we return the prefix up to that point.
    """
