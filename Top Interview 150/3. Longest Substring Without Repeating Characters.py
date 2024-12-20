# class Solution(object):
#     def lengthOfLongestSubstring(self, s): # produce wrong output for "dvdf" --> 2 instead of 3
#         """
#         :type s: str
#         :rtype: int
#         """
#         # idea 1: have 2 pointers
#         # initialization
#         index = 0
#         out = 0
#         local_out = 0
#         letters = set()

#         # iteration
#         while index < len(s):
#             if s[index] not in letters:
#                 local_out += 1
#                 letters.add(s[index])
#                 index += 1
#             else:
#                 out = max(out, local_out)
#                 local_out = 0
#                 letters = set()
#         out = max(out, local_out)
#         return out
                

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # idea 1: have 2 pointers
#         # initialization
#         index = 0
#         out = 0
#         local_out = 0
#         letters = set()

#         # iteration
#         while index < len(s):
#             if s[index] not in letters:
#                 local_out += 1
#                 letters.add(s[index])
#                 index += 1
#             if s[index - 1] in letters or index >= len(s):
#                 out = max(out, local_out)
#                 local_out = 0
#                 letters = set()
#                 index += 1
#         return out


# from collections import defaultdict # doesn't work

# class Solution(object):
#     def lengthOfLongestSubstring(self, s): # "dvdf"
#         """
#         :type s: str
#         :rtype: int
#         """
#         # evalluation:
#         # - time complexiity: O(n^2) --> because u restart from after the repeating index again
#         # - space complexity: O(n)
#         # initialization
#         index = 0 
#         myDict = defaultdict(int)
#         out = 0
#         local_out = 0

#         # iteration
#         while index < len(s):
#             if s[index] not in myDict:
#                 myDict[s[index]] = index
#                 index += 1
#             elif s[index] in myDict and myDict[s[index]] == index:
#                 index += 1
#             else:
#                 local_out = len(myDict)
#                 out = max(local_out, out)
#                 myDict[s[index]] = index
#                 index += 1

        # return out
        
# from collections import defaultdict

# class Solution(object):
#     def lengthOfLongestSubstring(self, s): # "dvdf"
#         """
#         :type s: str
#         :rtype: int
#         """
#         # evalluation:
#         # - time complexiity: O(n^2) --> because u restart from after the repeating index again
#         # - space complexity: O(n)
#         # initialization
#         index = 0 
#         myDict = defaultdict(int)
#         starting_index = 0
#         out = 0
#         local_out = 0

#         # iteration
#         while index < len(s):
#             while index < len(s) and s[index] not in myDict: # 1 < 4 and v not in mydict
#                 myDict[s[index]] = index # v = 1
#                 local_out += 1 # 2
#                 index += 1 # 2
#             out = max(out, local_out) # 2
#             local_out = 0 # 
#             if index < len(s): # 2 < 4
#                 index = myDict[s[index]] + 1 # 1
#             myDict = defaultdict(int) # 
#         return out

from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s): # "dvdf"
        """
        :type s: str
        :rtype: int
        """
        # idea1: have both front index and back index --> sliding window approach
        # initialization
        front_index = 0
        back_index = 0
        myDict = defaultdict(int)
        out = 0
        local_out = 0

        # iteration
        while back_index < len(s): # 0 < 4
            while back_index < len(s) and ((s[back_index] not in myDict) or (s[back_index] in myDict and myDict[s[back_index]] < front_index)): # 4 < 4 and f not in mydict
                myDict[s[back_index]] = back_index # d = 2, v = 1, f = 3
                back_index += 1 # 4
            out = max(out, back_index - front_index) # 3
            if back_index < len(s):
                front_index = myDict[s[back_index]] + 1 # 0 + 1 = 1
                myDict[s[back_index]] = back_index # d = 2, v = 1
                back_index += 1 # 3

        return out

