
# class Solution(object): # logical error
#     def jump(self, nums): # [2,3,1,1,4]
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # confirm fact
#         # - you can't iterate backwards (i cant proove that if theres a way forward, theres a way backwards)
#         # - so the only way is to iterate forward

#         # idea: for every step we take, the next step that will be chosen will be the farthest step

#         # initialization
#         last_ele_index = len(nums) - 1 # 4
#         num_jumps = 1
#         curr_index = 0
#         curr_max_jump = 0 # furthest jump it can possibly go
#         prev_max_jump = curr_index + nums[curr_index] # prev furthest jump i could go # 0 + 2 = 2

#         # iterating through the array
#         while curr_index < last_ele_index and curr_max_jump <= last_ele_index: # 3 < 4 and 4 < 4
#             prev_max_jump = curr_index + nums[curr_index] # 3 + 1 = 2
#             num_jumps += 1 # 2
#             curr_max_jump = prev_max_jump # 2
#             curr_index += 1 # 1
#             while (curr_index < last_ele_index and curr_index <= prev_max_jump and curr_max_jump < last_ele_index): # 3 < 4 and 3 <= 2
#                 if curr_max_jump < (curr_index + nums[curr_index]): # 4 < (2 + 1)
#                     curr_max_jump = nums[curr_index] # 4
#                 curr_index += 1 # 3
#             prev_max_jump = curr_max_jump  # 4



#         return num_jumps - 1


class Solution:
    def jump(self, nums):
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= (n - 1):
                return jumps + 1
            if i == current_end: # only add jumps if haven't reach the last index
                jumps += 1
                current_end = farthest
        
        return jumps
    
# note:
# - keep multiple pointers or trackers
# - this solution is like BFS, can you see it?