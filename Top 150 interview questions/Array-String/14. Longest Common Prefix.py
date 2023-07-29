class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            print(strs[i].find(prefix))
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

"""
The time complexity of the given program is O(n * m), where n is the length of the input list strs and m is the average length 
of the strings in strs. This is because the program iterates through each character of the strings in strs to find the 
longest common prefix.

Space Complexity O(1)
"""
