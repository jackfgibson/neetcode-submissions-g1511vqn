class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        
        while l<=h:
            m = (l+h)//2
            if nums[m]==target:
                return m
            if nums[m] >= nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if target <= nums[h] and target >= nums[m]:
                    l=m+1
                else:
                    h=m-1
        return -1

