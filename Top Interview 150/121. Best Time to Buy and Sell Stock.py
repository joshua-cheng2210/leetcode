# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
        # evaluation
        # - time complexity: O(n ^ 2)
        # - space complexity: O(n)
        
#         # idea: iterate through the list
#         # have another list keep track of the biggest selling value it has seen

#         # initialization
#         tracking = {}
#         max_profit = 0

#         # iteration
#         for i in range(len(prices)):
#             for key in tracking.keys():
#                 profit = prices[i] - key
#                 if profit > tracking[key]:
#                     tracking[key] = profit
#                     if profit > max_profit:
#                         max_profit = profit
#             tracking[prices[i]] = 0

#         return max_profit
            

# certain facts:
# - it has to run on time complexity O(n)
# - you cannot loop through the list again just to check the biggest difference for each number

# unsure facts:
# - how?

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         # logically flawed
#         # idea: iterate through the list, and 
#         # find the smallest and biggest value, 
#         # and also make sure that the index of the small val < index of the biggest value

#         # initialization
#         if (len(prices) <= 1):
#             return 0
        
#         # val = {"smallest_val" : 10^5 + 1,
#         #         "smallest_index" : len(prices),
#         #         "biggest_val" : -1, 
#         #         "biggest_index" : 0}
        
#         val = {"smallest_val" : prices[0],  # logically flawed: assigning the first value as the smallest or biggest val as it might not provide the best selling value
#                 "smallest_index" : len(prices),
#                 "biggest_val" : prices[0],
#                 "biggest_index" : 0}
        
#         for index in range(0, len(prices)):
#             if prices[index] < val["smallest_val"] and index < val["biggest_index"]:
#                 val["smallest_val"] = prices[index]
#                 val["smallest_index"] = index

#             if prices[index] > val["biggest_val"] and index > val["smallest_index"]:
#                 val["biggest_val"] = prices[index]
#                 val["biggest_index"] = index

#         return val["biggest_val"] - val["smallest_val"]

# [7, 1, 2, 6, 3, 5]
# [1, 2, 6, 3, 5]

# facts:
# - val["smallest_index"] < val["biggest_index"]

# alternative method (logically flawed: look at last example)
# - sort the prices list --> compare from the start & end of the list (assuming you can sort in under O(n))
# example after sorted()
# before_sorted   : [10, 1, 2, 4] --> 1 & 4
# key             : [1, 2, 4, 10]
# index           : [1, 2, 3, 0] --> index 3 - index 1 --> search from the end, so long as the index(end) > index(start) return the diff (logically flawed: look at last example)

# before_sorted   : [1, 10, 2, 4] --> 1 & 10
# key             : [1, 2, 4, 10]
# index           : [0, 2, 3, 1] --> index 1 - index 0

# before_sorted   : [5, 10, 1, 4]
# key             : [1, 4, 5, 10]
# index           : [2, 3, 0, 1] 


# method 3
# what if we have a function that returns a list like this. for example
# [1, 10, 2, 4] --> [[1, 10], [2, 4]]
# [11, 1, 10, 2, 4] --> [[11], [1, 10], [2, 4]] 
# [10, 1, 2, 4] --> [[1, 2, 4]]
# [5, 10, 1, 4] --> [[5, 10], [1, 4]]
# [8, 10, 1, 7] --> [[8, 10], [1, 7]]
# [0, 5, 10, 1, 4, 11] --> [[0, 5, 10], [1, 4, 11]]
# [12, 0, 5, 10, 1, 4, 15] --> [[12], [0, 5, 10], [1, 4, 15]]
# [-5, 11, 9, 12, 0, 5, 10, 1, 4, 15] --> [[-5, 11], [9, 12], [0, 5, 10], [1, 4, 15]]
# [-5, 11, 10, 9, 12, 0, 5, 10, 1, 4, 15] --> [[-5, 11], [10], [9, 12], [0, 5, 10], [1, 4, 15]]
# [-5, 11, 10, 9, 12, 0, -10, 5, 10, 1, 4, 15] --> [[-5, 11], [10], [9, 12], [0], [-10], [5, 10], [1, 4, 15]] # format A

# # logic B
# [[1,2], [3,4]] (smaller, smaller) --> take [first index, of first list, second index of econd list]
# [[1,2], [0,4]] (bigger, smaller) --> take the second list (obvious)
# [[1,4], [2,3]] (smaller, bigger) --> take the first list (obvious)
# [[1,3], [0,2]]  (bigger, bigger) --> take 2nd?



# # logic C
# [[2, 4], [x]]
# - if x > 4 --> it will never happen
# - if x < 2 --> compare it with the next list?
# - if 2 < x < 4 --> compare it with the next list?

# # logic D
# [[x], [2, 4]]
# - if x > 4 --> 
# - if x < 2 --> it will never happen
# - if 2 < x < 4 -->

# # logic C & D
# [[a, b], [x], [d, e]], where x < b && x > d
# [x < a] --> i cant imagine what to do
# [x > a, x < b] --> can ignore x
# [x > d, x < e] --> can ignore x
# [x > e] --> i cant imagine what to do

# [[2, 10], [0,4]]  (bigger, bigger) --> take the bigger range
# [[2, 10], [x], [0,4]]
# x > 10 --> won't happen
# x == 9 --> ignore
# x > e --> (x > b? wont happen : (y > a? ignore))
# # hold on, you should try to figure out what happens if compare with the front list
# x < a --> compare it with the in next list. but what if the next list is also len() == 1? 

# # logic E
# [[x], [y]]

# # format B
# [[1,3], [0,2]] --> take whichever range is bigger. but moving forward, compare with the second list
# [[3,5], [1,4], [0, 2]] 

# initialization
# iterate through the loop and break it down into format A while also applying logic B

# if you have a single digit inner list


# you should end up with format B --> choose the biggest range
# question: 
# - when do you change your smallest number?

# method 4
# - what if you do recursion?

# # method 5
# 1) sort the list
# 2) iterate from both ends until you find the biggest difference and also end index is more than the start index

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         # prices = list(prices)
#         def get_last_index_of_num(num):
#             return prices_length - list(reversed_prices).index(num) - 1
        
#         # initialization
#         prices_length = len(prices)
#         if prices_length <= 1:
#             return 0
#         sorted_prices = sorted(prices)
#         reversed_prices = reversed(prices)

#         # iterating through the loop
#         start_index = 0
#         end_index = prices_length - 1
#         index_difference = get_last_index_of_num(prices[end_index]) > get_last_index_of_num(prices[start_index])
#         profit = 0

#         while (index_difference > 0 and end_index > start_index):
#             # profit = prices[end_index] - prices[start_index]
#             if (sorted_prices[(end_index - 1)] - sorted_prices[(start_index)] > sorted_prices[(end_index)] - sorted_prices[(start_index + 1)]):
#                 end_index -= 1
#             else:
#                 start_index += 1


#             index_difference = get_last_index_of_num(sorted_prices[end_index]) > prices.index(sorted_prices[start_index])
        
#         profit = sorted_prices[end_index] - sorted_prices[start_index]
#         return profit


# solution (not mine - i couldn't figure it out)
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         buy = prices[0]
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] < buy:
#                 buy = prices[i]
#             elif prices[i] - buy > profit:
#                 profit = prices[i] - buy
#         return profit
    

class Solution(object): # kinda hard to understand the local min and max and aso the global min and max
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        localMax = 0
        globalMin = prices[0]
        maxMax=0
       
        for i in prices:
            if i <globalMin:
                globalMin = i
                localMax = i
            elif i > localMax:
                localMax = i
                maxMax = max(localMax - globalMin,maxMax)

        return maxMax


# note
# - identify what you definitely know
#   - if you want to find the optimal value like the max profit in this case, your algorithm is definitely going to be O(n) since the you need to make comparison with every number in the list and also if the list is not sorted]
#   - figure out if you actually need to remember the previou value that has already been iterated through
#   - maybe its hard to visualise the problem with a list, try drawing a graph