# class Solution(object):
#     def minSubArrayLen(self, target, nums): # you falsely understood the question
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         # idea 1: to sort the array and then chose the last few biggest number --> O(nlog(n))
#         # question: 
#         # - do we have to iterate through all the numbers? yes
#         # - pattern: its going to be the last biggest few numbers in nums
#         # - is there a O(n) method?

#         # idea2: O(n)
#         # iteration
#         # [] --> sum = target --> meta information like the smallest number
#         # [1,2,3,4,5], [5]
#         # [1] --> target_remaining = 5 - 1 = 4; target_size = 0
#         # [1,2] --> target_remaining = 5 - 1 = 4 - 2 = 2; target_size = 0
#         # [1,2,3] --> target_remaining = 5 - 1 = 4 - 2 = 2 - 3 = -1; target_size = 3
#         # [1,4] --> target_remaining = 
#         # question: how can i know that [4] > [2,3]? do i keep track of the biggest numbers in the list?

#         # idea1: 
#         # initialization
#         nums = sorted(nums, reverse=True) # you can't sort it cause the question wants the position of the elements in nums to be the same
#         out = []
#         out_size = 0
#         sum = 0

#         # iteration
#         for i in nums:
#             out.append(i)
#             sum += i
#             out_size += 1
#             if sum >= target:
#                 return out_size
#         return 0

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # evaluation
        # - time complexity: O(n)
        # - space complexity: O(1)
        # idea3: bruteforce: O(n^2) --> for eveyr number --> iterate forward until you get a sum of >= target

        # idea4: 
        out = float("inf")
        front_index = 0
        back_index = 0
        sum = 0
        if max(nums) >= target:
            return 1
        
        # iteration
        # while the sum of the numbers between the front and the back < target --> back_index += 1
        while back_index < len(nums):
            while sum < target and back_index < len(nums):
                sum += nums[back_index]
                back_index += 1

            while sum >= target and front_index < back_index:
                if sum >= target:
                    out = min(out, back_index - front_index)
                sum -= nums[front_index]
                front_index += 1
                
        if out == float('inf'):
            return 0
        return out

# note:
# - read the question properly. you falsely understood 209. maybe try to ask clarifying question next time? and try to amke statements about your understanding?
# - sliding window problem is just iterating through the array with front and back index