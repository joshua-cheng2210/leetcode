# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # initialization
#         front_index = 0
#         back_index = len(numbers) - 1

#         # iteration until front > back(front --> <--back) question: when to front+= 1 and back -= 1
#         while front_index < back_index:
#             if numbers[front_index] + numbers[back_index] == target:
#                 return [front_index + 1, back_index + 1]
#             else:
#                 front_increment = numbers[front_index + 1] + numbers[back_index] # flawed logic
#                 back_decrement = numbers[front_index] + numbers[back_index - 1]
#                 if front_increment < back_decrement:
#                     front_index += 1
#                 else:
#                     back_index -= 1

#         return [-1, -1]

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # initialization
        front_index = 0
        back_index = len(numbers) - 1

        # iteration until front > back(front --> <--back) question: when to front+= 1 and back -= 1
        while front_index < back_index:
            if numbers[front_index] + numbers[back_index] == target:
                return [front_index + 1, back_index + 1]
            else: # overly complex
                front_complement = target - numbers[front_index]
                back_complement = target - numbers[back_index]
                if front_complement > numbers[back_index] or back_complement > numbers[front_index]:
                    front_index += 1
                elif front_complement < numbers[back_index] or back_complement < numbers[front_index]:
                    back_index -= 1

        return [-1, -1]

# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         L,R = 0, len(numbers) - 1
#         while L < R:
#             if numbers[L] + numbers[R] == target:
#                 return [L+1,R+1]
#             elif numbers[L] + numbers[R] > target:
#                 R -= 1
#             else:
#                 L += 1
        
