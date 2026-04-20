class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        ans = 1
        for i in range(len(digits)):
            multi = 10**i
            ans += digits[i]*multi
        return list(map(int, str(ans)))