class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0 ,0
        cap = 0
        l, r = 0, len(height)-1
        while l<=r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if height[l] <= height[r]:
                cap = cap + maxL-height[l]
                l+=1
            else:
                cap = cap + maxR-height[r]
                r-=1
        return cap