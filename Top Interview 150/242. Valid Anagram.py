# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         # initialization
#         # iteration
#         for x in s:
#             if x not in t:
#                 return False
#             else:
#                 t = t.replace(x, '', 1)

#         if t != "":
#             return False
#         else:
#             return True

# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         s.sort()
#         t.sort()
#         return s == t
    
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         # evaluation:
#         # - time complexity: O(nlog(n) + mlog(m)) # assume the sorting function runs on nlog(n)
#         # - space complexity: O(1)
#         return sorted(s) == sorted(t)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        for char in list(set(s)):
            if s.count(char) != t.count(char):
                return False

        return True