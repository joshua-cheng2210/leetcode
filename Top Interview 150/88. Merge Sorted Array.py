class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # evaluation
        # time complexity = O(n) + O(m)
        # space complexity = O(1) # it is not O(n) + O(m) because you didn't create an additional temp array since you used nums1 array which was already given in the input

    #     temp_array = [0] * (m + n)  # you will never uniintentionally erase the num1 data before you put your final answer in num1 because there is enough space allocated to it
        temp_array_index = m + n - 1
        num1_index = m - 1
        num2_index = n - 1
        # skip the consecutive zeros from the back of num1
        while (num2_index >= 0 and num1_index >= 0):
        # iterate from the back of both num1 and num2
            if nums2[num2_index] >= nums1[num1_index]:
                nums1[temp_array_index] = nums2[num2_index]
                num2_index -= 1
            else:
                nums1[temp_array_index] = nums1[num1_index]
                num1_index -= 1
            temp_array_index -= 1

        while (num2_index >= 0):
            nums1[temp_array_index] = nums2[num2_index]
            num2_index -= 1
            temp_array_index -= 1
        # temp_array, num1_index and num2_index should be -1 here

# note:
# - be careful with indexing