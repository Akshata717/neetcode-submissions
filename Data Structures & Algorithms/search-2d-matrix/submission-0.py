class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [item for sublist in matrix for item in sublist]

        left = 0
        right = len(flat_list) - 1

        while left <= right:
            m = (left + right) // 2

            if (flat_list[m] < target):
                left = m + 1
            
            elif (flat_list[m] > target):
                right = m - 1
            
            else:
                return True
        
        return False
        