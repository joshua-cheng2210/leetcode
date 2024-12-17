class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # keep iterating and finding the characters in the needle s in haystack t
        for needle in s:
            index = t.find(needle)
            if index == -1:
                return False
            t = t[index + 1:]
        return True