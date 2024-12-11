class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return " ".join(s.split()[::-1])

# note:
# - using reverse() is slower than using list[::-1]
