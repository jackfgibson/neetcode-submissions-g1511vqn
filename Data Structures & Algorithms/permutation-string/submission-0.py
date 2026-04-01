class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1: return s1 in s2
        if len(s2) < len(s1): return False
        l, r = 0, len(s1)-1
        check = Counter(s1)

        while r<len(s2):
            if Counter(s2[l:r+1]) == check:
                return True
            l+=1
            r+=1
        return False