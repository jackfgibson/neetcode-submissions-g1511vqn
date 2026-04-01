class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for x in range(len(nums)):
            want = target-nums[x]
            if want in seen:
                return [seen[want], x]
            seen[nums[x]] = x