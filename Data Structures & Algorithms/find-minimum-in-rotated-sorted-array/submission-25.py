class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        m = (l+h)//2

        while l<h:
            if nums[m] > nums[h]:
                l = m+1
                m = (l+h)//2
            elif nums[m] < nums[h]:
                h = m
                m = (l+h)//2
        return nums[m]