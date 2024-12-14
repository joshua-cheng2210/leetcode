# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         # iterating through the array. how? and do what on each iteration? --> iterate starting from index 1


# [1,2,3,4] -> [24,12,8,6]
# idea 1: idk
# [2,3,4] -> [12, 8, 6]
# initialization:
# have the answer array default to [1, for len(nums)]

# # iteration"
# [2,3,4]
# iteration index: 0 --> 2
# do: 
# - do nothing on index 0?
# - remember index 0 element --> prev_num = 2
# - O(n^2) function --> would multiply the index value to all the element in answer except that index
# - mem_array = [2]

# iteration index 1 --> 3
# do:
# - 
# - mem_array = [2, 6]

# iteration index 2 --> 4
# do:
# - 
# - mem_array = [2, 6, 12]

# idea 2: initialization O(2n) --> iterating both front and back of the array
# [1,2,3,4] -> [24,12,8,6]
# initialization:
# iterate from front to back of the array
# prefix = 1
# prefix_array
# [1, 1, 2, 6]
# suffix = 1
# suffix_array
# [1, 4, 12, 24] --> reverse() --> [24, 12, 4, 1]

# iteration:
# [1 * 24, 1 * 12, 2 * 4, 6 * 1] --> return this
# [1,2,3,4] -> [24,12,8,6]
# class Solution(object): # implementing idea 2
#     def productExceptSelf(self, nums): # [1,2,3,4]
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         # evaluation:
#         # - time complexity: O(n)
#         # - space complexity: O(n)
#         # initialization
#         prefix = 1
#         prefix_array = [1]
#         for i in range(len(nums) - 1): # i = 2 < 3
#             prefix = prefix * nums[i] # 6
#             prefix_array.append(prefix) # [1, 1, 2, 6]

#         suffix = 1
#         suffix_array = [1]
#         for i in range(len(nums) - 1, 0, -1): # i = 0 > 0
#             suffix = suffix * nums[i] # 24
#             suffix_array.append(suffix) # [1, 4, 12, 24]


#         # iteration: 
#         for i in range(len(prefix_array)):
#             prefix_array[i] = prefix_array[i] * suffix_array[len(nums) - 1 - i]

#         return prefix_array

# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         # iterating through the array. how? and do what on each iteration? --> iterate starting from index 1


# [1,2,3,4] -> [24,12,8,6]
# idea 1: idk
# [2,3,4] -> [12, 8, 6]
# initialization:
# have the answer array default to [1, for len(nums)]

# # iteration"
# [2,3,4]
# iteration index: 0 --> 2
# do: 
# - do nothing on index 0?
# - remember index 0 element --> prev_num = 2
# - O(n^2) function --> would multiply the index value to all the element in answer except that index
# - mem_array = [2]

# iteration index 1 --> 3
# do:
# - 
# - mem_array = [2, 6]

# iteration index 2 --> 4
# do:
# - 
# - mem_array = [2, 6, 12]

# idea 2: initialization O(2n) --> iterating both front and back of the array
# [1,2,3,4] -> [24,12,8,6]
# initialization:
# iterate from front to back of the array
# prefix = 1
# prefix_array
# [1, 1, 2, 6]
# suffix = 1
# suffix_array
# [1, 4, 12, 24] --> reverse() --> [24, 12, 4, 1]

# iteration:
# [1 * 24, 1 * 12, 2 * 4, 6 * 1] --> return this
# [1,2,3,4] -> [24,12,8,6]

class Solution(object): # implementing idea 2
    def productExceptSelf(self, nums): # [1,2,3,4] -> [24,12,8,6]
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # evaluation:
        # - time complexity: O(n)
        # - space complexity: O(n)
        # initialization
        prefix = 1
        prefix_array = [1]
        for i in range(len(nums) - 1): # i = 2 < 3
            prefix = prefix * nums[i] # 6
            prefix_array.append(prefix) # [1, 1, 2, 6]

        suffix = 1
        suffix_array = [1]
        for i in range(len(nums) - 1, 0, -1): # i = 3 --> 2 --> 1 > 0
            suffix = suffix * nums[i] # 1 * 4 * 3 * 2
            prefix_array[i - 1] = prefix_array[i - 1] * suffix # [24, 12, 8, 6]

        return prefix_array
    
    # room for optimization:
    # - if theres 1 zero in nums --> return a list of only applying the alg on that index
    # - if theres 2 zeros in nums --> return a list of zeros of length(nums)

# note:
# - understand the pattern to get the answer for 1 element by 1) know what information you need 2) think how to get the information