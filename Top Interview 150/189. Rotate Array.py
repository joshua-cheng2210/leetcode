class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # evaluation:
        # - time complexity: O(N)
        # - space complexity: O(1)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        