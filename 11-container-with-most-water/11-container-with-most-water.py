class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxsize = 0
        while l<r:
            short = min(height[l],height[r])
            cursize = (short)*(r-l)
            maxsize = max(cursize,maxsize)
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
                
        return maxsize