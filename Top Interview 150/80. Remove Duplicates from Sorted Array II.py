class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # evaluation
        # - time complexity: O(N)
        # - space complexity: O(1)

        # initialization
        counter = 0
        prev_val = {"None" : 0}
        index_to_arrange = 0

        # iterate through the list
        for i in range(len(nums)): # 1 3
            # if the val is not the same as the previous 
            if nums[i] not in prev_val:
                # increase counter
                counter += 1 # counter = 2
                # restart the prev_index to the new val and 0
                prev_val = {nums[i] : 1} # {1 : 1}
            # if the val is the same (existing int he prev_val dict)
            else:
                # if the val is 1
                if prev_val[nums[i]] == 1:
                    # increment it
                    prev_val[nums[i]] += 1
                    counter += 1
                # if the val is 2
                else:
                    continue
            # take this values and place it in the index_to_arrange
            nums[index_to_arrange] = nums[i] # [1,2,3] --? [1,2,3]
            # increment index_to_arrange
            index_to_arrange += 1

        return counter


# note:
# - i remembered what i did for the remove deplicate version 1
