class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            x = (l+r)//2
            ans = min(ans, nums[x])
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            else:
                if nums[x] > nums[r]:
                    l = x+1
                else:
                    r = x-1
        return ans