def solve(s,n,i):
    if(n < 0): return 0 
    return (ord(s[n])-ord('a')+1)*(20**i)+solve(s,n-1,i+1)
s=input()
n=len(s) 
print(solve(s,n-1,0))

"""
Time Complexity O(n)
- Here n is the length of the string. 
Space Complexity O(n)
- During recursion, the stack memory is used. The depth of the recursion here is depedent on the input length of the string.
"""
