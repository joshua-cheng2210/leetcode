# idea 1:
# initialization
# iterate through the height until you find the first peak. say height[x] = 10 (get the first peak)
# create a dictionary ----> try default dictionary
# total_water = 0

# iteration till the end of the list
# first while loop iterating down the graph and also check if the list has not ended
# for every number x --> dict[x] += peak - x, (if its > 0)

# second while loop iterating up the graph and also check if the list has not ended
# for every number x --> dict[x] += peak - x, (if its > 0)
# new_peak = x

# when you exit the second while loop (it means you have found the next peak)
# water += dictionary[keys], such that keys <= min(new_peak, old_peak or peak)
# old_peak = new_peak
# restart everything again and repeat until list ends



# from collections import defaultdict

# class Solution(object): # flawed logic: you only compared between neighboring peaks
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         # initialization
#         water = 0
#         old_peak = 0
#         old_peak_index = 0
#         new_peak = 0
#         new_peak_index = 0
#         index = 0
#         element = {"index" : index, "val" : height[index]}
#         # water_dict = defaultdict();
#         # trimming the ends
#         while ((index + 1) < len(height)) and height[index] <= height[index + 1]:
#             old_peak = height[index + 1]
#             old_peak_index = index + 1
#             index += 1
#             element = {"index" : index, "val" : height[index]}
        
#         trim_counter = 0
#         i = len(height) - 1
#         while (i > 0) and height[i - 1] >= height[i]:
#             trim_counter += 1
#             i -= 1

#         if trim_counter != 0:
#             height = height[::-trim_counter]

#         # iteration
#         while ((index + 1) < len(height)):
#             # going down the slope # assumption that the old_peak is <= new_peak
#             old_peak_index = index
#             while ((index + 1) < len(height)) and height[index] >= height[index + 1]:
#                 collect = old_peak - height[index + 1]
#                 if collect > 0:
#                     water += collect
#                     # water_dict[height[index]] += collect
#                 index += 1
#                 element = {"index" : index, "val" : height[index]}
#             # going up
#             while ((index + 1) < len(height)) and height[index] <= height[index + 1]:
#                 new_peak = height[index + 1]
#                 new_peak_index = index + 1
#                 collect = old_peak - height[index + 1]
#                 if collect > 0:
#                     water += collect
#                     # water_dict[height[index]] += collect
#                 index += 1
#                 element = {"index" : index, "val" : height[index]}
#             if new_peak < old_peak and old_peak_index < new_peak_index: # is old_peak > new_peak
#                 water -= (new_peak_index - old_peak_index) * (old_peak - new_peak)
#             old_peak = new_peak

#             # index += 1
#         return water


# idea2: get some meta info first
# initialization
# iterate through the list and find
# 1) all the peaks 
# 2) and the index it is at
# ex: 
# [0,1,0,2,1,0,1,3,2,1,2,1]
# [(1:1), (3:2), (7:3), (10,2)] --> metadata (index : peak) or (peak : index) --> question: how do i process this data???


# note: 
# - when you get a questions, which you're given a list input. try:
# 1) iterating multiple times front to back or back to front
# 2) for each element in the list, try seeing if there are any patterns between the elements to the left and right of it
# 3) try figuring out if it has anything got to do with the peaks or lows of the graph or 4) try local andgloabl minima and maxima

# idea3: apply 2) --> for every element, figure out what is the highest number of the elements on teh left and right. sum += for each element, x, where min(max_left, max_right) - x

class Solution:
    def trap(self, height):
        # initialization
        if len(height) == 0:
            return 0
        ans = 0
        size = len(height)
        left_max, right_max = [0] * size, [0] * size
        left_max[0] = height[0]
        for i in range(1, size):
            # update left max with current max
            left_max[i] = max(height[i], left_max[i - 1])
        # Initialize last height into right max
        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            # update right max with current max
            right_max[i] = max(height[i], right_max[i + 1])
        # iteration
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        # Return amount of trapped water
        return ans