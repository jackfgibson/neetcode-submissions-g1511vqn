class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        k = (lo+hi)//2
        min_k = hi
        
        while lo<=hi:
            total = 0
            for pile in piles:
                total += -(pile//-k)
            if total<=h:
                min_k = min(min_k, k)
                hi = k-1
                k = (lo+hi)//2
            else:
                lo = k+1
                k = (lo+hi)//2
        return min_k


        # iterate through piles. time per pile is -(piles[i]//-k)
        # add each time per pile up
        # if it exceeds h, increase k, if it is less, decrease k
        # keep track of minimum k that was below h
        # return that min k