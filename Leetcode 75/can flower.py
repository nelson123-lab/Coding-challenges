class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        l, r, m = 0, 1, 2
        length = len(flowerbed)
        a = 0
        while l < len(flowerbed)-2:
            if flowerbed[l] == 0 and flowerbed[r] == 0 and (l == 0 and r == 1):
                flowerbed[l] = 1
                a += 1
            elif flowerbed[l] == 0 and flowerbed[r] == 0 and flowerbed[m] == 0:
                flowerbed[r] = 1
                a += 1
            elif flowerbed[r] == 0 and flowerbed[m] == 0 and (l == length-2 and r == length-1):
                flowerbed[m] = 1
                a += 1
            else:
                pass
            l += 1
            r += 1
            m += 1
        return a == n

ans = Solution()
print(ans.canPlaceFlowers(flowerbed = [0,0,1,0,1], n = 1))