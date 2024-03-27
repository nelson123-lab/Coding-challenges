# Solution from a youtube video.
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


# More understandable version.
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1]  < -a : 
                    s.pop()
                elif s[-1]  > -a : 
                    break
                else: 
                    s.pop()
                    break
            else: 
                s.append(a)
        return s

"""
- Here the main idea is to remove any asteriod that has less power to the left when a negative power appears. 
eg: [5, 6, -10] gonna return [] since the -10 is gonna remove both 5 and 6. That's why we are using a while loop within the for loop to check the power of the asteriod.

Time COmplexity O(n) even in the worst case scenario the input list will be processed only once.
Space Complexity O(n)
"""
