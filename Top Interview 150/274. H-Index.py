        

# known fact
# - it will output h where the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
# - h <= len(citations)
# - h <= max(citations)

# example:
# [3,0,6,1,5] --> 3
# [0,-3,3,-2,2] (-3)
# [-1,-4,2,-3,1] (-4)


# idea1
# iterate through every element. --> time_O(n)
# see if the element k is the output? --> finding at least k elements with k citations
    # create a new sorted_array? --> space_O(n), time_O(n^2)

# idea2 --> simpler to implement
# sorted the list --> time_O(n^2)
# iterate from left to right to see if element k is the output?

# class Solution(object): # logical error
#     def hIndex(self, citations): # [1,2,6,4,5]
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         # initialization
#         sorted_list = sorted(citations) # [1,2,4,5,6]
#         length = len(sorted_list) # 5
#         num_numbers_greater_than_h = length
#         h = 0

#         # iteration
#         while h <= length - 1 and num_numbers_greater_than_h > 0 and h <= sorted_list[-1]: # 1 <= 4 and 4 > 0
#             while (sorted_list[-num_numbers_greater_than_h] < h): # 1 < 1
#                 num_numbers_greater_than_h -= 1
#             if h > num_numbers_greater_than_h: # 0 > 4
#                 return h - 1
#             if ((h + 1 > length - 1)):
#                 break
#             if (h > sorted_list[-1]):
#                 break
#             h += 1 # 1
        
#         return h

# [1,2,3,4,5]: h = 1

# class Solution(object): 
#     def hIndex(self, citations): # [1,2,6,4,5]
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         # initialization
#         sorted_list = sorted(citations)
#         length = len(sorted_list)
#         h = 0

#         # iteration
#         while h <= sorted_list[-1] and h < length - 1:


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # evaluation:
        # - time complexity: O(n)
        # - space complexity: O(1)
        # Sort the list in descending order
        citations.sort(reverse=True)

        # Iterate and find the maximum h where citations[h-1] >= h
        h = 0
        for i, cite in enumerate(citations):
            if cite >= i + 1:
                h = i + 1
            else:
                break

        return h
    
# note:
# - maybe not iterate the answer?
# - the solution was really good at determining what is the pattern of the answer. (i.e. 1)h < len(citations) 2)h satisfies the h-index definition)

# Explanation
# Sorting in Descending Order:

# Sorting the citations in descending order ensures that we can easily compare the number of citations with the index.
# Iterating Through Sorted List:

# The i+1 represents the number of papers considered so far.
# If the citation count (c) is greater than or equal to i+1, then this is a valid h. Otherwise, we break out of the loop.
# Output the Maximum Valid h:

# The value of h keeps track of the highest valid h-index encountered during iteration.
# Example Walkthrough
# Input: [3,0,6,1,5]
# Sorted in descending order: [6, 5, 3, 1, 0]
# Iteration:
# i=0, c=6: c >= i+1 → h=1
# i=1, c=5: c >= i+1 → h=2
# i=2, c=3: c >= i+1 → h=3
# i=3, c=1: c < i+1 → Stop
# Return h=3.
# Input: [1,3,1]
# Sorted in descending order: [3, 1, 1]
# Iteration:
# i=0, c=3: c >= i+1 → h=1
# i=1, c=1: c < i+1 → Stop
# Return h=1.
