class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # evaluation
        # - time complexity: O(n)
        # - space complexity: O(1)

        # initialization
        total_profit = 0
        buy = prices[0] 
        sell = None
        index = 1
        # iterating through the list
        while index < len(prices): 
            # while the price is going down --> change the buy value to the lower value
            while (index < len(prices) and prices[index] <= prices[index - 1]): 
                buy = prices[index] 
                index += 1 
            # while the price is going up --> remember the highest selling value
            while (index < len(prices) and prices[index] > prices[index - 1]): 
                sell = prices[index] 
                index += 1 
            if sell != None:
                total_profit += sell - buy
                sell = None

        return total_profit
    
# note:
# - i think its easier than the level 1 version of this question

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         buy = prices[0]
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > buy:
#                 profit += prices[i] - buy
#             buy = prices[i]
#         return profit

# note:
# - so this solution is adding many small changes rather than my solution that adds little big changes - how is adding small changes faster? is it because i have too many if statements and checkings?
        