class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if (x < 0):
        #     return False
        xx = str(x)
        xx2 = xx[::-1]
        return xx == xx2

        # if (x < 0):
        #   return False
        
        # reverse_num = 0
        # temp = x

        # while (temp != 0):
        #   digit = temp % 10
        #   reverse_num = reverse_num * 10 + digit
        #   temp = temp // 10

        # return x == reverse_num
