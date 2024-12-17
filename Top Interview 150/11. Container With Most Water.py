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
            while front_index < back_index and :
