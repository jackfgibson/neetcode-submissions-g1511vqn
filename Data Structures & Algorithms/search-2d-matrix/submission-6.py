class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, h = 0, rows-1
        row = (l+h)//2
        while l<=h:
            if target>=matrix[row][0] and target<=matrix[row][-1]:
                l, h = 0, cols-1
                m = (l+h)//2
                while l<=h:
                    if matrix[row][m]==target:
                        return True
                    elif matrix[row][m]<target:
                        l = m+1
                        m = (l+h)//2
                    else:
                        h = m-1
                        m = (l+h)//2
            elif target>matrix[row][-1]:
                l=row+1
                row=(l+h)//2
            else:
                h=row-1
                row=(l+h)//2
        return False