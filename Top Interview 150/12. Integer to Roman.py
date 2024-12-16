# idea1,
# have a preset dictionary
# keep iterating from the biggest number of the dictionary and dividing num until you get 0
class Solution(object):
    def intToRoman(self, num):
        """
        ,type num, int
        ,rtype, str
        """
        # initialization
        num_list = [(1000,"M"), 
                     (900,"CM"),
                     (500,"D"),
                     (400,"CD"),
                     (100,"C"),
                     (90,"XC"),
                     (50,"L"),
                     (40,"XL"),
                     (10,"X"),
                     (9,"IX"),
                     (5,"V"),
                     (4,"IV"),
                     (1,"I")]
        index = 0
        output =""
        # iteration
        while index < len(num_list) and num > 0:
            if num > 0 and (num // num_list[index][0] >= 1):
                counter = num // num_list[index][0]
                num = num % num_list[index][0]
                output += (num_list[index][1] * counter)
            index += 1
        return output


        
    