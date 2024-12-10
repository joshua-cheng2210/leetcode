class Solution(object):
    def canJump(self, nums): # [4, 1, 2, 0, 0, 0]
        """
        :type nums: List[int]
        :rtype: bool
        """
        # initialization
        steps = 0
        index = 0
        if len(nums) == 1:
            return True
        # iterating through the list
        while index < len(nums) - 1:
            # if the number on that list is > steps. replace the steps
            steps = max(steps, nums[index])
            # if the steps reaches 0 before reaching the end, return false

            if steps == 0:
                return False
            
            # steps -= 1 for moving every index forward
            steps -= 1
            index += 1

        return True
        
# note:
# - be sure on the priority of the decision making. which factor is the most important. reaching the last index or if you reach step == 0? 
# - you must get use to debugging your own before spamming the debugger