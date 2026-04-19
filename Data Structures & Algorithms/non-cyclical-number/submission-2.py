from functools import reduce

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        res = n
        while res not in seen:
            seen[res] = 1
            total = 0
            for char in list(str(res)):
                total+= int(char)**2
            if total == 1: return True
            res = total
        return False