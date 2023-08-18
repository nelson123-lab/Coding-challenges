"""
Problem Statement  :

Here is about to introduce a new kind of number system. Where instead of 10 digits there is 20, from a to t, all in small. Now a means 1, b means 2 and t means 20, thenn aa means 21. Now for  
a new number you have to print the decimal form it.

Note that the letters in the input string will be lower case and from a to t. 

Input Format:
Single line containing the string of new number system’s number

Output Format:
Single line denoting the integer with the same decimal value as the input string

Sample input 1: e
Sample Output: 5

Sample  Input 2: ac
Sample Output: 23
"""

def convert_to_decimal(new_number):
    decimal_value = 0
    base = 20

    for i in range(len(new_number)):
        letter = new_number[i]
        numerical_value = ord(letter) - ord('a') + 1
        decimal_value += numerical_value * (base ** (len(new_number) - i - 1))

    return decimal_value

# Example usage:
new_number1 = 'e'
print(convert_to_decimal(new_number1))  # Output: 5

new_number2 = 'aa'
print(convert_to_decimal(new_number2))  # Output: 23

"""
Time Complexity O(n)
- Here the time complexity is depeneded on the input of the string.
Space Complexity O(1)
- Output is independent of the input.
"""

"""
Solution using recursion.
"""
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
