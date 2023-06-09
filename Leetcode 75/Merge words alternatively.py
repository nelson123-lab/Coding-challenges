class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
     # Checking for largest string
        if len(word1) > len(word2):
            l,s = word1, word2
        else:
            l,s = word2, word1
       
    # Initializing an empty string.
        al_str = ""
        
        # Iterating through the smaller string and adding the strings alternatively and finally adding the remaining elements of the largest word.
        for i in range(len(s)):
            al_str += word1[i] + word2[i]
        return al_str + l[len(s):len(l)]
