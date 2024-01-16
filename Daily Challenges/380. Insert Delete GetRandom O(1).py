class RandomizedSet(object):

    def __init__(self):
        self.nummap = {}
        self.numlist = []

    def insert(self, val):
        if val not in self.nummap:
            self.nummap[val] = len(self.numlist)
            self.numlist.append(val)
            return True
        else:
            return False
        

    def remove(self, val):
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
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.numlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
