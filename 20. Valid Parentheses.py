class Solution(object):
    # def isValid(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """

    #     # evaluation:
    #     # - time complexity: O(n)
    #     # - space complexity: O(n)

    #     brackets = {
    #         '(' : ')',
    #         '[' : ']',
    #         '{' : '}'
    #     }
    #     open_brackets_tracking = ""
    #     closing_brackets_tracking = ""
    #     # iterating through the list
    #     for c in s:
    #         if (c == '}' or c == ')' or c == ']') and open_brackets_tracking == "":
    #             return False
    #     # if its a close bracket,
    #         if (c == '}' or c == ')' or c == ']'):
    #             if (c != closing_brackets_tracking[-1]):
    #                 return False
    #             else:
    #                 # do the necessary changes
    #                 open_brackets_tracking = open_brackets_tracking[:-1]
    #                 closing_brackets_tracking = closing_brackets_tracking[:-1]
                    
    #     # check if it is the same as the expected_closing_brackets
    #     # if no, return false
    #     # if yes, update the expected_closing_bracket to the next ne
    #     # if the list is not a bracket, skip and continue
    #         elif c not in brackets:
    #             continue
    #     # else
    #         else:
    #     # if its a open bracket
    #             if (c == '{' or c == '(' or c == '['):
    #     # add it to the brackets
    #                 open_brackets_tracking += c
    #                 closing_brackets_tracking += brackets[c]
    #     # update the expected_closing_brackets

    #     if open_brackets_tracking != "" and closing_brackets_tracking != "":
    #         return False

    #     return True
        

    def isValid(self, s):
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in brackets:
                top = stack.pop() if stack else "#"
                if brackets[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
    
# note: 
# - utilize stack