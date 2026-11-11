class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (row * cols) - 1

        while left <= right:
            m = (left + right) // 2
            row = m // cols
            col = m % cols

            if (matrix[row][col] < target):
                left = m + 1
            
            elif (matrix[row][col] > target):
                right = m - 1
            
            else:
                return True
        
        return False
        