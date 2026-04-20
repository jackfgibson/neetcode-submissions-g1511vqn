class Solution:
    def countBits(self, n: int) -> List[int]:
        def ones(num):
            one = 0
            while num:
                num = num & num-1
                one+=1
            return one
        ans = []
        for i in range(n+1):
            ans.append(ones(i))
        return ans