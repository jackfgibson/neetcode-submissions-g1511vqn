class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        unique = set()
        longest = 0
        l, r = 0, 1
        unique.add(s[l])
        while r<len(s):
            if s[r] in unique:
                while s[l]!=s[r]:
                    unique.discard(s[l])
                    l+=1
                l+=1
            unique.add(s[r])
            longest = max(longest, len(unique))
            r+=1
        return longest