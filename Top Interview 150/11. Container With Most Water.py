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
