# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # evaluation:
#         # - time complexity: O(N)
#         # - space complexity: O(N) # because you created a dictionary to store the information 
#         # have a dictionary_counter
#         dict_counter = {}
#         # get the len of nums list
#         n = len(nums)
#         thrashold = (n // 2 + n % 2)

#         # iterate through the list
#         for i in nums:
#             # if the nums exist in the dict ii> += 1
#             if i in dict_counter:
#             # check if the nums >= n / 2
#                 dict_counter[i] += 1
#             else:
#             # else add it to the list
#                 dict_counter[i] = 1
#             if dict_counter[i] >= thrashold:
#                     return i

# if the answer get the length of the array at the star, check other language solution.

# class Solution(object):
    # evaluation
    # - time complexity: im not sure what sorting algorithm they are using
    # - space complexity: O(n)
#     def majorityElement(self, nums):
#        nums.sort()
#        n=len(nums)
#        return nums[n//2]

# Boyer-Moore Voting Algorithm # if you're sure the item's occurance you're looking for is more that half of the search space, this is your alg
# evaluation
# - time complexity: O(n)
# - space complexity: O(1)
class Solution:
 def majorityElement(self, nums):
  candidate, count = None, 0
  for num in nums:
   if count == 0:
    candidate = num
   count += 1 if num == candidate else -1
  return candidate