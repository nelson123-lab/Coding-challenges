class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l, r, m = 0,1, 2
        a = 0
        while l< len(flowerbed)-2:
            if flowerbed[l] == 0 and flowerbed[r] == 0 and flowerbed[m] == 0:
                flowerbed[r] = 1
                a += 1
            else:
                pass
            l += 1
            r += 1
            m += 1
        return a == n