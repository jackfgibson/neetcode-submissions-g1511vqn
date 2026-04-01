class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [x for row in matrix for x in row]
        l, h = 0, len(flat)-1
        m = (l+h)//2
        while l<=h:
            if flat[m]==target:
                return True
            elif flat[m]>target:
                h = m-1
                m = (l+h)//2
            else:
                l = m+1
                m = (l+h)//2
        return False