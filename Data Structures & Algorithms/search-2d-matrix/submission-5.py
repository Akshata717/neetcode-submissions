class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while (left <= right):
            m = (left + right) // 2
            r = m // cols
            c = m % cols

            if (matrix[r][c] < target):
                left = m + 1

            
            elif (matrix[r][c] > target):
                right = m - 1
            
            else:
                return True
        
        return False
        