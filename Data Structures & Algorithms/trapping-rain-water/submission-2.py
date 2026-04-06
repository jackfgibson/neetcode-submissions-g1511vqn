class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL = 0
        maxR = 0
        total = 0
        #move pointer with lower max value inwards
        #water trapped = min(maxL,maxR)-height[i]
        while l<=r:
            if maxL<=maxR:
                total += max(min(maxL, maxR)-height[l], 0)
                maxL = max(maxL, height[l])
                l+=1
            else:
                total += max(min(maxL, maxR)-height[r], 0)
                maxR = max(maxR, height[r])
                r-=1
        return total