import random
class RandomizedSet(object):
# idea
# - use some sort of hash format
    def __init__(self):
        # evaluation:
        # - time complexity: O(n)
        # - space complexity: O(n)
        self.hashSize = 1031
        self.hashArray = [[] for _ in range(self.hashSize)] 
        self.nonEmptyHashIndex = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # evaluation:
        # - time complexity: O(1)
        # - space complexity: O(n)
        hashIndex = val % self.hashSize
        if self.hashArray[hashIndex] == None:
            self.hashArray[hashIndex] = [val]
        else:
            for i in self.hashArray[hashIndex]:
                if i == val:
                    return False
            self.hashArray[hashIndex] += [val]
            self.nonEmptyHashIndex += [hashIndex]
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # evaluation:
        # - time complexity: O(1)
        # - space complexity: O(1)
        hashIndex = val % self.hashSize
        if self.hashArray[hashIndex] != None:
            for i in self.hashArray[hashIndex]:
                if i == val:
                    self.hashArray[hashIndex].remove(val)
                    self.nonEmptyHashIndex.remove(hashIndex)
                    return True

        return False

            
    def getRandom(self):
        """
        :rtype: int
        """
        # evaluation:
        # - time complexity: O(1)
        # - space complexity: O(1)
        temp_array = self.nonEmptyHashIndex
        temp = len(self.nonEmptyHashIndex)
        randomHashIndex =  self.nonEmptyHashIndex[int(random.random() * len(self.nonEmptyHashIndex))]

        temp_array = self.hashArray[randomHashIndex]
        temp = len(self.hashArray[randomHashIndex])
        randomIndex = int(random.random() * len(self.hashArray[randomHashIndex]))
        return self.hashArray[randomHashIndex][randomIndex]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# from collections import defaultdict

# class RandomizedSet(object):

#     def __init__(self):
#         self.locs = defaultdict(int)
#         self.container = []

#     def insert(self, val):
#         """
#         :type val: int
#         :rtype: bool
#         """
#         # it keeps the value as a key in the defaultdict() and add it to the array; and then it keeps the index of the item in the array as the value in the defaultdict()
#         if val not in self.locs:
#             self.locs[val] = len(self.container)
#             self.container.append(val)
#             return True
#         return False
        

#     def remove(self, val):
#         """
#         :type val: int
#         :rtype: bool
#         """
#         if val not in self.locs:
#             return False
#         n = len(self.container)
#         vaLoc = self.locs[val]
#         tail = self.container[n-1]
#         self.container[vaLoc], self.container[n-1] = self.container[n-1], self.container[vaLoc]
#         self.locs[tail] = vaLoc
#         self.container.pop()
#         del self.locs[val]
#         return True
        

#     def getRandom(self):
#         """
#         :rtype: int
#         """
#         return random.choice(self.container)
        


# note:
# - an advance version of the normal dictionary data structure - defaultdict()
# - normal dict will not edit the value of a non-existant key in the dict; but for defaultdict(), it will automatically initialize the key and set the value
# - it keeps the value as a key in the defaultdict() and add it to the array; and then it keeps the index of the item in the array as the value in the defaultdict() - this can make insert() and del() a time of O(1) but of course space of O(n)
# - idea is use both a dictionary and an array to have O(1) in search, add and del. Using a dictionary to keep track of the index of the element in a normal array
