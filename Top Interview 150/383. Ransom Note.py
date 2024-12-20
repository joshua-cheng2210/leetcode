from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
# idea1: the bruteforce --> O(n + m)
# idea2: if we sort both note and mag --> O(nlog(n) + mlog(m)) + O(n + m)

        # initialization
        # if the length of the note > magazine --> return false
        if len(ransomNote) > len(magazine):
            return False
        # create a dictionary counter for the magazine
        myDict = defaultdict(int)
        for c in magazine:
            myDict[c] += 1

        # iteration
        # on every char in the mag --> -1 in teh dict --> if dict < 0 --> return false
        for c in ransomNote:
            myDict[c] -= 1
            if myDict[c] < 0:
                return False
            
        return True

        
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         alphabet = [0] * 26
#         for c in ransomNote:
#             idx = ord(c) - ord('a')
#             i = magazine.find(c, alphabet[idx])
#             if i == -1:
#                 return False
#             alphabet[idx] = i + 1
#         return True

# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
        
#         for char in ransomNote:
            
#             if char in magazine:
#                 magazine = magazine.replace(char, "", 1)
#             else:
#                 return False
#         return True