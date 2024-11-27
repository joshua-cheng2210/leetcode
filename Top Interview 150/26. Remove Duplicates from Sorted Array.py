class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # evaluation
    #     # - time complexity: O(n)
    #     # - space complexity: O(1)
    #     # so have 2 pointers. 1 for iterating through the list and the other for updating the list
    #     updating_index = 1
    #     counter = 1
    #     if len(nums) <= 1:
    #         return len(nums)
    #     for i in range(1, len(nums)):
    #         if nums[i] != nums[updating_index - 1]:
    #             nums[updating_index] = nums[i]
    #             updating_index += 1
    #             counter += 1
    #     return counter

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = nums
        nums2 = sorted(list(set(nums2)))
        counter = len(nums2)
        nums[:counter] = nums2[:counter]

        return counter
          

            
nums = [1,1,2]
assert Solution.removeDuplicates(Solution, nums) == 2, "testing"
assert nums == [1,2,2]


