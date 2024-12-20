from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # evaluation:
        # - time complexity: O(n)
        # - space complexity: O(n)
        # idea1: for every character read in s, read the same positioned char in t and stored it in a dict
        # initialization
        myDict = defaultdict(chr)
        mapped_values = set()
        s_index = 0

        # iteration
        while s_index < len(s):
            if s[s_index] not in myDict:
                if t[s_index] in mapped_values:
                    return False
                myDict[s[s_index]] = t[s_index]
                mapped_values.add(t[s_index])
            elif myDict[s[s_index]] != t[s_index]:
                return False
            s_index += 1

        return True
