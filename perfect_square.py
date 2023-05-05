def perfect_square(n):
    if n< 0:
        return False
    else:
        b =1
        while n/b > b:
            print(n/b,b)
            b += 1
        return n/b * n/b == n
print(perfect_square(25))
# print(perfect_square(14))
