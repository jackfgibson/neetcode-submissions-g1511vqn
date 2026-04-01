class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1: return s1 in s2
        if len(s2) < len(s1): return False
        l, r = 0, len(s1)-1
        check = Counter(s1)
        window = Counter(s2[l:r+1])

        while r<len(s2):
            if window == check:
                return True
            window[s2[l]]-=1
            l+=1
            r+=1
            if r<len(s2):
                window[s2[r]]+=1
        return False