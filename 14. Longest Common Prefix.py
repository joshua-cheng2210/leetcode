class Solution(object):
    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     # assumption
    #     # - strs is never empty (but if its empty we can return "")

    #     # evaluation
    #     # time complexity: O(n)
    #     # space complexity: O(1) or O(n)

    #     if len(strs) == 0:
    #         return ""
    #     # have the returning prefix as the first index
    #     prefix = min(strs)
    #     prefix_index = len(prefix)

    #     # iterate through the strings in str
    #     for str in strs:
    #     # iterate through the characters in the string
    #         index = 0
    #         while index < prefix_index and index < len(str) and prefix[index] == str[index]:
    #     # reduce the prefix to the first few similar characters
    #             index += 1
    #         prefix_index = index
    #         if prefix_index == 0:
    #             return ""

    #     prefix = prefix[:index]
    #     return prefix

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(min(strs))
        prefix = ""
        for j in range(length):
            letter = strs[0][j]
            for i in range(1,len(strs)):
                if letter != strs[i][j]:
                    return prefix
            prefix += letter
        return prefix    

# note:
# - try to not search unnecessary search space