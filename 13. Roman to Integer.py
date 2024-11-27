class Solution(object):
    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     # assumptions:
    #     # - these characters will be in capital letters

    #     # evaluations:
    #     # time complexity = O(N)
    #     # space complexity = O(1) 
    #     # shouldn't it be O(n)?
    #     # thats because you're not adding memory by adding the sum for each character. the variable sum doesn't expand in size as it adds more number or roman character
        
    #     # create dictionary # question: is it better to hardcode IV and the special cases? - create a special_num_dict?
    #     num_dict = {
    #         "I" : 1,
    #         "V" : 5,
    #         "X" : 10,
    #         "L" : 50,
    #         "C" : 100, 
    #         "D" : 500,
    #         "M" : 1000
    #     }
    #     sum = 0
    #     if len(s) == 0:
    #         return sum

    #     # iterate through all the characters on the string
    #     index = 0
    #     end = len(s)
    #     while index < end:
    #         # check if that character is smaller than the next character
    #         if (index + 1) < end and num_dict[s[index]] < num_dict[s[index + 1]]:
    #             # take the next character and subtract that current chracter
    #             sum += (num_dict[s[index + 1]] - num_dict[s[index]])
    #             index += 2
    #         # else
    #         else:
    #         # convert the character to integer and add it to the sum
    #             sum += (num_dict[s[index]])
    #             index += 1


    #     return sum
                
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 
            'L': 50, 'C': 100, 
            'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_values[char]
            if current_value < prev_value:
                total -= current_value  # Subtract if smaller value precedes larger one
            else:
                total += current_value
            prev_value = current_value
        
        return total
    

# note:
# - sometimes try thinking about iterating the list backwards