class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # objective: maximize distance between indexes between bars and heights
        # calculation: multiply distances between indexes and min(heights)
        # create containers: combination of bars: 1+2, 1+3, 1+4, ..., 3+4, 3+5, etc
        max_water = 0
        for side_A_ind in range(0, len(heights)-1):
            for side_B_ind in range(1, len(heights)):
                if side_A_ind < side_B_ind:
                    area_container = (min(heights[side_A_ind], heights[side_B_ind]) * 
                        (side_B_ind - side_A_ind)
                    )
                    if area_container > max_water:
                        max_water = area_container
        return max_water