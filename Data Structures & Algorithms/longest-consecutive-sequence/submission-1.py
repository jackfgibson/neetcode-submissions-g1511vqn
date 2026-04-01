class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in (0, 1):
            return len(nums)
        longest, curr = 1, 1
        s = set(nums)
        for n in nums:
            if n-1 not in s:
                num = n
                while num+1 in s:
                    curr+=1
                    num+=1
                longest = max(longest, curr)
                curr = 1
        return longest
