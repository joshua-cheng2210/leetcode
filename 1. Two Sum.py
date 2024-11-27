class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution 1: bruteforce method -> O(n^2)
        # i = 0
        # while (i < len(nums) ):
        #     j = 0
        #     while (j < len(nums)):
        #         if (nums[i] + nums[j] == target and i != j):
        #             return [i, j]
        #         j+=1
        #     i+=1
        # return []

# solution 2: O(n^2) but at least it doesnt have to enter the loop if its complement doesn't exist in the loop
        # i = 0
        # while (i < len(nums)):
        #     finding = target - nums[i]
        #     if (finding in nums):
        #         j = 0
        #         while (j < len(nums)):
        #             if (nums[i] + nums[j] == target and i != j):
        #                 return [i, j]
        #             j+=1
        #     i+=1
        # return []

# solution 3: preventing calling the len(nums) function multiple times to prevent inefficiency... but it doesn't seem to affect it very much
        # i = 0
        # length_of_nums = len(nums)
        # while (i < length_of_nums):
        #     finding = target - nums[i]
        #     if (finding in nums):
        #         j = 0
        #         while (j < length_of_nums):
        #             if (nums[i] + nums[j] == target and i != j):
        #                 return [i, j]
        #             j+=1
        #     i+=1
        # return []


# solution 4: (Two-pass Hash Table)
        # numMap = {}
        # n = len(nums)

        # # Build the hash table
        # for i in range(n):
        #     numMap[nums[i]] = i

        # # Find the complement
        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in numMap and numMap[complement] != i:
        #         return [i, numMap[complement]]

        # return []  # No solution found


# solution 5: (One-pass Hash Table)
        # numMap = {}
        # n = len(nums)

        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in numMap:
        #         return [numMap[complement], i]
        #     numMap[nums[i]] = i

        # return []  # No solution found


# solution 6: trying my own map function
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [i, numMap[complement]]
            numMap[nums[i]] = i
        return []





















