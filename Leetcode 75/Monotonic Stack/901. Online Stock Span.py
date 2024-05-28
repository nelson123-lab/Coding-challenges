class StockSpanner(object):

    def __init__(self):
        self.st = []

    def next(self, price):
        span = 1
        while self.st and self.st[-1][0] <= price:
            span += self.st.pop()[1]
        self.st.append((price, span))
        return span

"""
Approach
The StockSpanner class has a stack of pairs of integers, where the first integer represents the stock price, and the second integer represents the span of that price.
The constructor of the class does not take any arguments and does not do anything.
The next() method of the class takes an integer argument price, which represents the price of the stock for the current day, and returns an integer representing the span of that price.
Initially, the span is set to 1.
If the stack is not empty and the top of the stack has a price less than or equal to the current price, then the span is increased by the span of the top of the stack, and the top of the stack is popped.
The pair of the current price and its span is pushed onto the stack.
Finally, the span of the current price is returned.
Complexity:
The time complexity of the next function is O(N), where N is the number of calls to next. This is because in the worst case, all the elements in the stack will be popped out before the current price is pushed onto the stack.
The space complexity of the algorithm is O(N), as we are storing all the prices and their corresponding span values in the stack.

Credits: Leetcode solution[https://leetcode.com/problems/online-stock-span/solutions/3391419/c-java-python-javascript-monotonic-stack-question-explained-in-simple-words]
"""
