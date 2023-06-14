class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        l, r, m = 0, 1, 2
        length = len(flowerbed)
        a = 0
        if length == 1 and flowerbed[l] == 0:
            flowerbed[l] = 1
            a += 1
        elif length == 2 and flowerbed[l] == 0 and flowerbed[r] == 0:
            flowerbed[l] == 1
            a += 1
        while length > 2 and l < length-2:

            if flowerbed[l] == 0 and flowerbed[r] == 0 and flowerbed[m] == 0:
                if length == 3:
                    flowerbed[l], flowerbed[m] = 1, 1
                    a += 2
                elif length == 5 and flowerbed[m+1] == 0:
                    flowerbed[l], flowerbed[m] = 1, 1
                    a += 2
                else:
                    flowerbed[r] = 1
                    a += 1
            elif flowerbed[l] == 0 and flowerbed[r] == 0 and (l == 0 and r == 1):
                flowerbed[l] =1
                a += 1
            elif flowerbed[r] == 0 and flowerbed[m] == 0 and (r == length-2 and m == length-1):
                flowerbed[m] = 1
                a += 1
            else:
                pass
            l += 1
            r += 1
            m += 1
        return a >= n

ans = Solution()
print(ans.canPlaceFlowers(flowerbed = [0,0,0,0,1], n = 2))