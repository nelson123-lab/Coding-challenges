"""
Ashish was copying from Rahit in the exam. So, Rahit told him to change the answers a little bit so that the examiner cannot find the fraud. But silly Ashish in the way started to 
change all the answers that were needed. He shuffled the letters in each word in a way where the maximum number of letters were misplaced For a given word, find the maximum difference that Ashish can generate between his answer and Rahit’s answer.

Suppose Rahit wrote “car” for an answer, Ashish can write “acr” with difference 2, or “arc” with differnece 3.

Note That: The letters are all in lowercase.

Input Format:

First line containing an integer n, number of words.
Then, n numbers of lines as the query words.

Output:
N number of lines with an integer each denoting possible maximum difference.

Sample Input:

4
abababa
bbj
kj
kk

Sample Output:

6
2
2
0
"""

from itertools import permutations

def solve(x, n):
    res = 0
    for word in permutations(x):
        count = 0
        for i in range(n):
            if x[i] != word[i]:
                count += 1
        res = max(res, count)
    return res

a = int(input())
for i in range(a):
    s = input()
    print(solve(s, len(s)))

"""
Time Complexity O(n!)
- This is because for a loop within the loop permutations are taken when works in O(n!) compelxity.
Space COmplexity O(n!)
- Doing permutations take O(n!) space.
"""
