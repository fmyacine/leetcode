class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix) , len(matrix[0])
        for i in range(rows):
            start = 0
            end = cols - 1
            while(start <= end):
                mid = (start + end ) // 2
                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    start = mid + 1
                else:
                    end = mid - 1 
        return False