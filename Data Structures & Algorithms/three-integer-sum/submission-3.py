class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            need = -nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                if nums[l]+nums[r]==need:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                elif nums[l]+nums[r]>need:
                    r-=1
                else:
                    l+=1
        return ans