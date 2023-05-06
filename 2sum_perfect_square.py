import math
 
def isPerfectSquare(x):
    if(x >= 0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return False


def solution(numbers):
    numbers = sorted(numbers)
    res = 0
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            add = numbers[i]+numbers[j]
            if add>=0 and isPerfectSquare(add) == True: res += 1
    return res

print(solution([-2, -1, 0, 1, 2]))
# solution




s