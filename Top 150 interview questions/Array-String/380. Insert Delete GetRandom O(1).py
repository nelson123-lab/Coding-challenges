class RandomizedSet:

    def __init__(self):
        self.nummap = {}
        self.numlist = []

    def insert(self, val: int) -> bool:
        if val not in self.nummap:
            self.nummap[val] = len(self.numlist)
            self.numlist.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.nummap:
            idx = self.nummap[val]
            lastVal = self.numlist[-1]
            self.numlist[idx] = lastVal
            self.numlist.pop()
            self.nummap[lastVal] = idx
            del self.nummap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.numlist)
        # random.choice(list) is a method to generate random numbers

"""
The main complexity in the problem is to do the do the operations in O(1). 
- When we are using a HashMap inserting into the list after cheking in the hashmap can be done in O(1).
- Removing in O(1) is a complex process. If we are finding the value from the list and removing it would taking time Complexity more than
O(1). Instead we swap between the values and delete it and brink it back. This operation can be done in O(1)
"""
