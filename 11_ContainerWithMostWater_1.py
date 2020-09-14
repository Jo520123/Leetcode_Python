class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        result = 0

        while l < r:
            water = min(height[l], height[r])*(r-l)

            if water > result:
                result = water

            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return result