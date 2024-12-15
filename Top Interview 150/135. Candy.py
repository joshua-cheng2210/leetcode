# [1,2,3,4,5] --> [1,2,3,4,5]
# [1,2,4,5,6] --> [1,2,3,4,5]
# [1,2,3,4,5,3,4] --> [1,2,3,4,5,1,2]
# [1,2,3,4,5,3,2] --> [1,2,3,4,5,2,1]
# idea: if it went up n steps. (add 1 --> n); if its went down n steps (add 1 --> n)
# [1,2,3,2,1,0] --> [1,2,3,2,1,0] --> [1,2,4,3,2,1] (learn: something tells me that my idea works if i iterate from the back)
# [1,2,3,2,1,0,1,2,3,2,1,0] -->
# [1,2,3,4,5,6,5,4,2,1] --> [1,2,3,4,5,6,4,3,2,1] (learn: iterating backwards would meet the same specail case too)
# [0,1,2,3,4,5,6,5,4,2,1] --> []
# [1,2,3,2,1,0] --> 
# [1,2,3,2,1,0]
# lowest_val = 1
# elemens_considered = 5

# [1,2,1,0,1,2,3,2,1,0,-1,1,2,3,4]
# [5,6,5,4,5,6,7,6,5,4,3] --> -min() = 3 --> [2,3,2,1,2,3,4,3,2,1,0] (learn: simplified question)
# [2,3,2,1,2,3,4,3,2,1,0] --> [3,4,3,2,3,4,5,4,3,2,1] (correct ans)
# [1,2,1,0,1,2,3,2,1,0,-1] + 2 --> [3,4,3,2,3,4,5,4,3,2,1] (my ans)
# index = 1
# lowest_val = 2
# max_candy_given = 2

# [2,3,2,1,2,3,6,5,4,3,2,1,0]
# min_val = 0
# max_val = 6
# range = 6 - 0 + 1 = 7
# max_awarded_candy = 3 (if awarding_candy >= max_awarded_candy -->add steps)
# increasing_steps = 2 --> 1
# decreasing_steps = 3 (while going down, if give 0 candy, += decreasing_steps)
# [2,3,2,1,2,3,6,5,4,3,2,1,0]
# [1,2,1,2]
# +(decreasing_steps - 1 = 3 - 1)

# class Solution(object): # flawed logic somewhere
#     def candy(self, ratings):
#         """
#         :type ratings: List[int]
#         :rtype: int
#         """
#         # initialization
#         awarding_candies = 1
#         increasing_steps = 1
#         decreasing_steps = 1
#         index = 1
#         min_candies = 1
#         min_candies_array = [1]

#         # iteration
#         while (index < len(ratings)):
#             # while increasing
#             while (index < len(ratings) and ratings[index] > ratings[index - 1]):
#                 awarding_candies += 1
#                 min_candies += awarding_candies
#                 min_candies_array.append(awarding_candies)
#                 increasing_steps += 1
#                 index += 1
#             increasing_steps = 1
#             # while decreasing
#             while (index < len(ratings) and ratings[index] < ratings[index - 1]):
#                 awarding_candies -= 1
#                 if awarding_candies <= 0:
#                     min_candies += decreasing_steps
#                     min_candies_array.append(decreasing_steps)
#                 decreasing_steps += 1
#                 index += 1
#             # if decreased ended early
#             if awarding_candies > 0 and decreasing_steps > 1: # if awarding candies iterates [6,5] --> [6,1]; decresing_steps: [1,2]
#                 min_candies -= (decreasing_steps - 1) * (awarding_candies - 1)
#                 min_candies_array.append((decreasing_steps - 1) * (awarding_candies - 1) * -1)
#             decreasing_steps = 1
#             awarding_candies = 1
#             # if its the same
#             if (index < len(ratings) and ratings[index] == ratings[index - 1]):
#                 awarding_candies = 1
#                 min_candies += 1
#                 min_candies_array.append(1)
#                 index += 1
#         return min_candies


# class Solution(object): # improvement from the first attempt (more accurate)
#     def candy(self, ratings): # [2,3,2,1,2,3,4,3,2,1,0]
#         """
#         :type ratings: List[int]
#         :rtype: int
#         """
#         # initialization
#         back_index = 0
#         front_index = 0
#         min_candies = 0
#         awarding_candies = 1
#         increasing_steps = 1
#         decreasing_steps = 1
#         element = ratings[0]

#         # iteration
#         while (back_index < (len(ratings) - 1)): # back_index = 0 < 11
#             # same
#             while ((front_index + 1) <= (len(ratings) - 1)) and ratings[front_index] == ratings[front_index + 1]: #
#                 min_candies += 1
#                 front_index += 1
#             back_index = front_index

#             # increasing
#             increasing_steps = 1
#             awarding_candies = 1
#             while ((front_index + 1) <= (len(ratings) - 1)) and ratings[front_index] < ratings[front_index + 1]: # front_index = 6 # 1 < 2 < 3 < 4 !< 3
#                 element = ratings[front_index]
#                 min_candies += awarding_candies # 1 = 1; 7 + 1 + 2 + 3
#                 awarding_candies += 1 # 4
#                 increasing_steps += 1 # 4
#                 front_index += 1 # 6
#             if (decreasing_steps > 1) and (increasing_steps > 1):
#                 min_candies -= min(increasing_steps, decreasing_steps) #  7 + 1 + 2 + 3 + 4 = 17
#                 min_candies += max(increasing_steps, decreasing_steps) #  7 + 1 + 2 + 3 + 4 = 17
#             elif (decreasing_steps <= 1) and (increasing_steps > 1):
#                 min_candies += increasing_steps

#             back_index = front_index # 1
#             awarding_candies = 1 # 1
#             # decreasing
#             decreasing_steps = 1
#             awarding_candies = 1
#             while ((front_index + 1) <= (len(ratings) - 1)) and ratings[front_index] > ratings[front_index + 1]: # front_index = 3 # 3 > 2 > 1 !> 2
#                 element = ratings[front_index]
#                 min_candies += awarding_candies # 1 + 1 + 2
#                 awarding_candies += 1 # 3
#                 decreasing_steps += 1 # 3
#                 front_index += 1 # 3
#             if (increasing_steps > 1) and (decreasing_steps > 1):
#                 min_candies -= min(increasing_steps, decreasing_steps) # 1 + 1 + 2 + 3 = 7
#                 min_candies += max(increasing_steps, decreasing_steps) # 1 + 1 + 2 + 3 = 7
#             elif (increasing_steps <= 1) and (decreasing_steps > 1):
#                 min_candies += decreasing_steps
#             back_index = front_index # 3
#             awarding_candies = 1
#         return min_candies


# # idea 2: in the initialization: iterate 2 times. once forward and once backwards
# # initialization
# [2,3,2,1,2,3,4,3,2,1,0]
# [1,2,0,1,2,3,4,0,0,0,0] --> iterate forward and figure a way to get this array
# [0,3,2,1,0,0,5,4,3,2,1] --> iterate backwads and figure a way to get this array
# # iteration
# [1,3,2,1,2,3,5,4,3,2,1] --> output the bigger element of the 2 same index

# class Solution(object): # implementing idea 2
#     def candy(self, ratings): # [2,3,2,1,2,3,4,3,2,1,0]
#         """
#         :type ratings: List[int]
#         :rtype: int
#         """
#         # initialization
#         # increasing_array
#         length = len(ratings)
#         if length ==  1:
#             return 1
#         index = 0

#         increasing_array = []
#         increasing_points = 1
#         while (index < len(ratings) - 1): # flawed logic: [1,2,2] makes the increasing_array [1,0,0] instead of [1,2,0]
#             if (ratings[index] < ratings[index + 1]):
#                 increasing_array.append(increasing_points)
#                 increasing_points += 1
#             else:
#                 increasing_array.append(0)
#                 increasing_points = 1
#             index += 1
#         if (index == len(ratings) - 1) and (ratings[index - 1] < ratings[index]):
#             increasing_array.append(increasing_points)
#             increasing_points += 1
#         elif (index == len(ratings) - 1) and not (ratings[index - 1] < ratings[index]):
#             increasing_array.append(0)

        

#         # decreasing_array
#         decreasing_points = 1
#         decreasing_array = []
#         # if (ratings[-1] < ratings[-2]):
#         #     decreasing_array = [1]
#         #     decreasing_points += 1
#         index  = len(ratings) - 1
#         while ((index - 1) >= 0):
#             if (ratings[index - 1] > ratings[index]):
#                 decreasing_array.append(decreasing_points)
#                 decreasing_points += 1
#             else:
#                 decreasing_array.append(0)
#                 decreasing_points = 1
#             index -= 1
#         if (index == 0) and (ratings[0] > ratings[1]):
#             decreasing_array.append(decreasing_points)
#             decreasing_points += 1
#         elif (index == 0) and not (ratings[0] > ratings[1]):
#             decreasing_array.append(0)
#         decreasing_array = decreasing_array[::-1]
    
#         # iteration
#         index = 0
#         sum = 0
#         while (index < len(increasing_array)):
#             sum += max(increasing_array[index], decreasing_array[index], 1)
#             index += 1
        
#           return sum

# # idea 2: in the initialization: iterate 2 times. once forward and once backwards
# # initialization
# [2,3,2,1,2,3,4,3,2,1,0]
# [1,2,0,1,2,3,4,0,0,0,0] --> iterate forward and figure a way to get this array
# [0,3,2,1,0,0,5,4,3,2,1] --> iterate backwads and figure a way to get this array
# # iteration
# [1,3,2,1,2,3,5,4,3,2,1] --> output the bigger element of the 2 same index

class Solution(object): # improvement from the first attempt of idea2 (more accurate) # it finally fucking worked! spent like 4 hours total
    def candy(self, ratings): # [1,2,1]
        """
        :type ratings: List[int]
        :rtype: int
        """
        # evaluation
        # - time complexity: O(3n) --> O(n)
        # - space complexity: O(3n) --> O(n)
        # initialization
        length = len(ratings)
        if length == 1:
            return 1
        index = 0

        increasing_array = [0] * length
        increasing_points = 1
        # increasing array
        while (index + 1 < length):
            if ratings[index] < ratings[index + 1]:
                increasing_array[index] = increasing_points
                increasing_array[index + 1] = increasing_points + 1
                increasing_points += 1
            else:
                increasing_points = 1
            index += 1

        # decreasing array
        decreasing_array = [0] * length
        decreasing_points = 1
        index = length - 1
        while (index - 1 >= 0):
            if ratings[index - 1] > ratings[index]:
                decreasing_array[index] = decreasing_points 
                decreasing_array[index - 1] = decreasing_points + 1 # [2,1,0]
                decreasing_points += 1
            else:
                decreasing_points = 1
            index -= 1

        # iteration
        index = 0
        sum = 0
        while (index < len(increasing_array)):
            sum += max(increasing_array[index], decreasing_array[index], 1)
            index += 1
        
        return sum

# idea 2: in the initialization: iterate 2 times. once forward and once backwards
# initialization
# [2,3,2,1,2,3,4,3,2,1,0]
# [1,2,0,1,2,3,4,0,0,0,0] --> iterate forward and figure a way to get this array
# [0,3,2,1,0,0,5,4,3,2,1] --> iterate backwads and figure a way to get this array
# iteration
# [1,3,2,1,2,3,5,4,3,2,1] --> output the bigger element of the 2 same index

# note: 
# - some times to have a time complexit better than O(n^2), if you don't know how to only iterate the list once, try any methods like iterating the list multiple times but not for len(list) times
# - O(x n), where x < n, is still better than O(n^2). try iterating multiple times like front to back and back to front