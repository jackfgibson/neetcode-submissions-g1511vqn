class Solution:
    def trap(self, height: List[int]) -> int:
        l, r =  0, len(height)-1
        maxL, maxR = 0, 0
        trap = 0
        while l<=r:
            if maxL<=maxR:
                trap += max(maxL-height[l],0)
                maxL = max(maxL, height[l])
                l+=1
            else:
                trap += max(maxR-height[r],0)
                maxR = max(maxR, height[r])
                r-=1
        return trap
