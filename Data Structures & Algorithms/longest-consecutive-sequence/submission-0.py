class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        line = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in line:
                length = 1
                while num+length in line:
                    length += 1
                longest = max(longest, length)
        return longest