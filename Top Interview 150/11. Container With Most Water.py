class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # initialization
        front_index = 0
        front = {"index":0, "peak":0}
        back_index = len(height) - 1
        back = {"index":0, "peak":0}

        max_water = 0

        # iteration
        while front_index < back_index:
            water = min(height[front_index], height[back_index]) * (back_index - front_index)
            max_water = max(water, max_water)
            if height[front_index] < height[back_index]: # idk how to iterate the list
                front_index += 1
            else:
                back_index -= 1
            
        return max_water
    
# thought process
# 100% definite
# - have 2 pointers iterating from both ends of the array
# - the both pointers move towards each other

# 50% sure
# - idk how they are going to move towards each other (which one should take the closer step to each other)
# - idk which is more important factor? (height or width)?

# goal: 
# - get as much water as possible

# 2 main factor for collecting largest amount of water
# - height --> i think this
# - width 

# .
# ..
# ...
# ..
# .
# .
# how do you even compare width? if you move, you're moving one step closer to each other... --> so its height the more important factor?

# if height[]
