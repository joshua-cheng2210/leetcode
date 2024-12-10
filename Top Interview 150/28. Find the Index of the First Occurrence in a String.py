# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         # initialization
#         first_occurence_index = 0
#         haystack_index = 0
#         haystack_length = len(haystack)
#         needle_index = 0
#         needle_length = len(needle)

#         # iterate through the needle
#         while needle_index < needle_length and haystack_index < haystack_length: 
#             # if the character matches the needle, match the rest of the character in the needle
#             if (haystack[haystack_index] == needle[needle_index]): 
#                 needle_index += 1
#             else:
#                 if (haystack[haystack_index] == needle[needle_index]): # imperfect logic hadling special case
#                     haystack_index -= 1 # special case: haystack = "mississippi"; needle = "issip" # not solved # i would just create an additional function
#                 needle_index = 0 
#             # if all the characters in the needle matches, return the startign index
#             haystack_index += 1 
#         if needle_index == len(needle): 
#             return haystack_index - needle_length
#         else:
#             return -1
        

# note:
# - try practising debugging using comments. meaning comment the value of the variable to keep track of the value and verify your algorithm
# - use substring aproach

# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         # evaluation:
#         # - time complexity: O(N)
#         # - space compelxity: O(N)
#         haystack_list = str(haystack).split(needle)
#         if (len(haystack_list) == 1):
#             return -1
#         else:
#             return len(haystack_list[0])
        
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # evaluation:
        # - time complexity: O(N)
        # - space compelxity: O(1)

        needle_length = len(needle)
        
        for i in range(len(haystack)):
            if haystack[i : i + needle_length] == needle:
                return i
            
        return -1