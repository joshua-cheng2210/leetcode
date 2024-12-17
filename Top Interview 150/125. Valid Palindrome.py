# class Solution(object):
#     def isPalindrome(self, s): # "abccba", "abcba"
#         """
#         :type s: str
#         :rtype: bool
#         """
#         # initialization
#         # have a front pointer, back pointer
#         front_index = 0
#         back_index = len(s) - 1

#         # iteration
#         # iterate until back front pointer >= back pointer
#         while front_index < back_index:
#             while (front_index < back_index) and s[front_index].isalnum() == False:
#                 front_index += 1
#             while (front_index < back_index) and s[back_index].isalnum() == False:
#                 back_index -= 1
#             if (front_index < back_index) and s[front_index].lower() != s[back_index].lower():
#                 return False
#             else:
#                 back_index -= 1
#                 front_index += 1
#         return True
    
class Solution(object):
    def isPalindrome(self, s):
        # evaluation
        # time complexity: O(n) # note that this is not O(n^2) because when you use the .replace(), you go through the string s function by the length of the symbols_to_remove times (not by length of string s times)
        # space complexity: O(n)
        symbols_to_remove = ",!?.:@#_-+*/[]{}\''\";\\()` "
        for symbol in symbols_to_remove: 
            s = s.replace(symbol, "")
   
        n = s[::-1]
  
        return s.lower()==n.lower()

# note:
# - you might want to look at some common string manipulation build-in functions