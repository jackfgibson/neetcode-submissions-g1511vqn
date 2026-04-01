class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        longest = 0
        highfreq = 0
        counter = Counter()
        l, r = 0, 1
        counter[s[l]]+=1
        while r<len(s):
            counter[s[r]]+=1
            if counter[s[r]]>highfreq:
                highfreq = counter[s[r]]
            if r-l+1-highfreq<=k:
                longest = max(longest, r-l+1)
            else:
                counter[s[l]]-=1
                l+=1
            r+=1
            #maintain frequency of chars
            #keep track of highest freq
            #subtract highest freq from size of window
            #check if that is <= k, if so, it's good.
        return longest