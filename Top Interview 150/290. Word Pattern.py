from collections import defaultdict

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # question:
        # - the number of words in s == number of letters in pattern?

        # initializtion
        # split s by spaces
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        # have a dictionary
        myDict = defaultdict(str)
        # have a set of mapped values
        mapped_values = set()
        pattern_index = 0

        # iteration
        while pattern_index < len(pattern):
            if pattern[pattern_index] in myDict:
                if myDict[pattern[pattern_index]] != s[pattern_index]:
                    return False
            else:
                if s[pattern_index] in mapped_values:
                    return False
                else:
                    mapped_values.add(s[pattern_index])
                    myDict[pattern[pattern_index]] = s[pattern_index]
            pattern_index += 1

        return True
