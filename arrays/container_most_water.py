import numpy as np

class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        area = 0
    
        while l < r:
            # Calculating the max area
            area = max(area, min(height[l],
                                 height[r]) * (r - l))
    
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area


if __name__ == '__main__':
    sol = Solution()
    sol_area = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(sol_area)
