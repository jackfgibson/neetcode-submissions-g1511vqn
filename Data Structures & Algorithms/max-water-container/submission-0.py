class Solution:
    def maxArea(self, heights: List[int]) -> int:
        big = 0
        l, r = 0, len(heights)-1
        while l<r:
            cap = min(heights[l], heights[r])*(r-l)
            print(l, r, cap)
            if cap>big:
                big = min(heights[l], heights[r])*(r-l)
            else:
                if heights[r]>=heights[l]:
                    l+=1
                else:
                    r-=1
        return big