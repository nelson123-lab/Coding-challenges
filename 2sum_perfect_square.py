import math
 
def isPerfectSquare(x):
    if(x >= 0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return False

# def solution(numbers):
#     n = len(numbers)
#     numbers.sort()
#     a = set()
#     if n < 2:
#         if isPerfectSquare(2*numbers[0]):
#             a.add((0, 0))
#     for i in range(n):
#         k = n-1
#         while i<k:
#             add = numbers[i] + numbers[k]
#             if isPerfectSquare(2*numbers[i]):
#                 a.add((i, i))
#             if isPerfectSquare(2*numbers[k]):
#                 a.add((k, k))
#             if isPerfectSquare(add):
#                 a.add((i,k))
#                 k -= 1
#             else:
#                 k -= 1
#     return a

def solution(numbers):
    numbers = sorted(numbers)
    res = 0
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            add = numbers[i]+numbers[j]
            if add>=0 and isPerfectSquare(add) == True: res += 1
    return res

print(solution([-2, -1, 0, 1, 2]))
