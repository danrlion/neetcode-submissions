class Solution:
    def trap(self, height: List[int]) -> int:
        total_water_area = 0
        for i in range(1, len(height)-1):
            max_L = max(height[:i])
            max_R = max(height[i+1:])
            min_LR = min(max_L, max_R)
            water_level = min_LR - height[i]
            if water_level > 0:
                total_water_area += water_level

        return total_water_area


            
