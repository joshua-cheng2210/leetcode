# idea1: for every number, try to find the sum of its contra.
# [-1,0,1,2,-1,-4]
# element: -1
# contra: 0 - (-1) = +1

# initialization

# 100% know
# - idea1: brute force --> O(n^3) --> for every element A, iterate the list, such that for every element B, iterate the list again such that for every element C + B + A = 0 --> collect this set
# - at least time: O(n), space O(n) --> iterate the list only once
# - idea2: sort the nums?: O(n log(n))

# [-1,0,1,2,-1,-4] --> [-4,-1,-1,0,1,2]

# 50% sure
# - at least time: O(n), space O(n) --> iterate the list only once --> for every element A, --> do what?
# - i know that we can reduce time O(n^2) to time O(n) + space O(n^2) but can we reduce time O(n^3) to time O(n) + space O(n^?)?

# - how to iterate sorted list()?
# [-4,-1,-1,0,1,2]
# idea2a: for every num, have 2 pointers (front n back pointers moving towards each other until they find the contra or not) -4: front: -1 && back: 2
# idea2b: have 3 pointers (front n back n center) for every front pointer, if center + back > contra(front){back--} else{center++} front++ --> O(n^3)
# idea2c: have 2 pointers (front n back) while front < back: find the 3rd number {if the 3rd number is between front and back --> add to the set; if 3rd number > 0 --> back--; else front++} --> O(n^2)
# [4,1,1,0,-1,-2] --> contra

# goal
# - find 3 numbers tat provides sum of 0

# class Solution(object): # bruh you're not even trying
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # evaluation: 
#         # - time complexity: O(2^n) # unbounded recursion which is bad
#         # - space complexity: O(n + m)
#         # initialization
#         front_index = 0
#         back_index = len(nums) - 1
#         nums = sorted(nums)
#         out = []

#         # iteration
#         while front_index < back_index:
#             contra = 0 - nums[front_index] - nums[back_index]
            
#             # Fix the list slicing and membership check
#             if contra in nums[front_index + 1:back_index] and [nums[front_index], contra, nums[back_index]] not in out:
#                 out.append([nums[front_index], contra, nums[back_index]])
            
#             # Update the indices
#             if contra > nums[back_index]:
#                 front_index += 1
#             elif contra < nums[front_index]:
#                 back_index -= 1
#             else:
#                 # Correct recursive call syntax
#                 out += self.threeSum(nums[front_index + 1:back_index + 1])  
#                 out += self.threeSum(nums[front_index: back_index])
#                 break  # Prevent infinite recursion
        
#         out = list(set(map(tuple, out)))  # Convert inner lists to tuples, remove duplicates
#         out = [list(item) for item in out]  # Convert tuples back to lists

#         return out

# class Solution(object): 
#     def threeSum(self, nums): # bruh you were lazy to think detailly 
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # initialization
#         out = []
#         def twoSum(nums, target):
#             numMap = {}
#             n = len(nums)

#             for i in range(n):
#                 complement = target - nums[i]
#                 if complement in numMap:
#                     return [nums[i], complement]
#                 numMap[nums[i]] = i
#             return []
#         # iteration
#         for i in range(len(nums)):
#             target = 0 - nums[i]
#             complement = twoSum(nums[i+1:], target)
#             if complement != [] and [nums[i]] + complement not in out:
#                 out.append([nums[i]] + complement)
#         return out
        
# class Solution(object): # [-1,0,1,2,-1,-4]
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         def twoSum(nums, target):
#             # evaluation:
#             # - time complexity: O(n)
#             # - space complexity: O(n)
#             numMap = {}
#             out = []
#             n = len(nums)

#             for i in range(n):
#                 complement = target - nums[i]
#                 if complement in numMap and [nums[i], complement] not in out and [complement, nums[i]] not in out:
#                     out.append([nums[i], complement]) 
#                 numMap[nums[i]] = i
#             return out
        
#         n = len(nums) # 6
#         out = []
#         for a in range(n): # 0 
#             complement = 0 - nums[a] # 0
#             b_c = twoSum(nums - nums[a], complement)
#             for x in b_c:
#                 a_b_c = sorted([nums[a]] + x)
#                 if a_b_c not in out:
#                     out.append(a_b_c)
#         return out


# idea3: 
# from collections import defaultdict
# class Solution(object): # [-1,0,1,2,-1,-4]
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # initialization
#         # sort the nums
#         nums = sorted(nums)
#         n = len(nums)
#         numDic = defaultdict(list)
#         out = []

#         # for every element in nums: find its complement --> put it in dict complemetn : [indexes...]
#         for c in range(n):
#             complement = 0 - nums[c]
#             numDic[complement].append(c) # sum of a + b here
        
#         # iteration O(n^2)
#         # for every number a:
#         for a in range(n):
#             if nums[a] > 0:
#                 break
#             # for every number b: 1 index after a
#             for b in range(a + 1, n):
#                 a_b = nums[a] + nums[b]
#                 # find the last number c
#                 # if c is in dict:
#                 if a_b in numDic:
#                     c = numDic[a_b][0]
#                     for x in numDic[a_b]:
#                         if x != a and x != b:
#                             c = x
#                             break
#                     if c != a and c != b:
#                         sort = sorted([nums[a], nums[b], nums[c]]) 
#                         if sort not in out:
#                             out.append(sort)
#         return out


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: # uniquely cuts the search space
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]: # skip repeating lo number
                    lo += 1