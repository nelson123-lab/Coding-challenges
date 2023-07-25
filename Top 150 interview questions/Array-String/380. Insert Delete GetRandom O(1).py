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

"""
The main complexity in the problem is to do the do the operations in O(1). 
- When we are using a HashMap inserting into the list after cheking in the hashmap can be done in O(1).

"""
