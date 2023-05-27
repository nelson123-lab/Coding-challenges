# Function to check if quadruplet exists in a list with the given sum
def hasQuadruplet(nums, target):
 
    # create an empty dictionary
    # key —> target of a pair in the list
    # value —> list storing an index of every pair having that sum
    d = {}
 
    # consider each element except the last element
    for i in range(len(nums) - 1):
        # start from the i'th element until the last elements
        for j in range(i + 1, len(nums)):
            # calculate the remaining sum
            val = target - (nums[i] + nums[j])
            # if the remaining sum is found on the dictionary,
            # we have found a quadruplet
            if val in d:
                # check every pair having a sum equal to the remaining sum
                for pair in d[val]:
                    x, y = pair
                    # if quadruplet doesn't overlap, print it and return true
                    if (x != i and x != j) and (y != i and y != j):
                        print('Quadruplet Found', (nums[i], nums[j], nums[x], nums[y]))
                        return True
            # insert the current pair into the dictionary
            d.setdefault(nums[i] + nums[j], []).append((i, j))
 
    # return false if quadruplet doesn't exist
    return False
