import collections
class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)

"""
Here the values that is appended to the deque is checked each time whether it can make the particular request or not by checking it with t-3000.
Time complexity O(n)
- we iterate through the dequeue to remove elements that are older than t-3000.
Space Compexity O(n)
- The space used by the dequeue depends upon the type of input used.
"""
