class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, h = 0, cols-1
        for row in matrix:
            if target<=row[-1]:
                while l<=h:
                    mid = (l+h)//2
                    if row[mid]==target:
                        return True
                    elif row[mid]<target:
                        l = mid+1
                        mid = (l+h)//2
                    else:
                        h = mid-1
                        mid = (l+h)//2
        return False