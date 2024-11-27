class Solution(object):
    # def removeElement(self, nums, val):
    #     """
    #     :type nums: List[int]
    #     :type val: int
    #     :rtype: int
    #     """
    #     # get the length of the nums
    #     index = len(nums) - 1
    #     replace_index = -1 # todo: check if the list is empty

    #     counter = 0
    #     # iterate from the back of the num
    #     while (index >= 0):
    #     # if the number == val:
    #         if nums[index] == val:
    #     # set the number to the last index value
    #             while (nums[replace_index] == val):
    #                 replace_index -= 1
    #             nums[index] = nums[replace_index]
    #             replace_index -= 1
    #     # else
    #         else:
    #     # increase the counter
    #             counter += 1
    #         index -= 1

    #     return counter
        
    # def removeElement(self, nums, val):
    #     """
    #     :type nums: List[int]
    #     :type val: int
    #     :rtype: int
    #     """
    #     length = len(nums) 
    #     index = 0
    #     back_index = len(nums) - 1
    #     counter = 0
    #     # iterate through the list
    #     while (index < length and (index < back_index)):
    #     # if the num == val:
    #         if (nums[index] == val):
    #     # iterate from the back of the list until you find a number that != val
    #             while(back_index >= 0 and nums[back_index] == val):
    #                 back_index -= 1
    #     # replace that number with the front val
    #             nums[index] = nums[back_index]
    #             nums[back_index] = val
    #     # if the num != val:
    #         # if the num != val:
    #     # increase counter
    #         counter += 1
    #         index += 1

    #     return counter

    def removeElement(self, nums, val):
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
    
# note: 
# - instead of looking for the next val to be replace, the algorithm looked out for the next non-val to replace the val