class Solution:
    def asteroidCollision(self, asteroids):
        s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1] + a < 0: s.pop()
                elif s[-1] + a > 0: break
                else: s.pop(); break
            else: s.append(a)
        return s

a = Solution()
print(a.asteroidCollision([10,2,-5]))