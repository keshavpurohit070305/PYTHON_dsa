class Solution(object):
    def maxArea(self, height):
        m=0
        l = 0
        r = len(height) - 1

        while (l < r):
            a = min(height[l] , height[r]) * (r - l)
            m = max(a , m)

            if ( height[l] >= height[r]):
                r = r - 1

            else :
                l = l + 1
        return m
              

        