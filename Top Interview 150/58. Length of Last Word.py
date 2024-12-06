class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # evaluation
        # - time complexity: O(N)
        # - space complexity: O(1)
        
        return len(s.strip().split()[-1])
    
# note:
# - too easy
# - challenge: is it posssible to not use any in-built functions?