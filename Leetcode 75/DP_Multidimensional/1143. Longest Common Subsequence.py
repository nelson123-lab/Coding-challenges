class Solution(object):
    def longestCommonSubsequence(self, text1, text2):

        m, n = len(text1), len(text2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

"""
Here we are creating a multidimensional array with the shape of m and n which are the length of text 1 and text 2.
Looks for elements diagonally and if they matches then it's gets updated by one. 
Time Complexity O(m*n)
Space Complexity O(m*n)
"""
