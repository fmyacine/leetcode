bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    printf("%d %d",matrixSize , *matrixColSize);
    for(int i = 0; i < matrixSize ; i++){
        
        int start = 0, end = *matrixColSize - 1;

        while(start <= end){

            int mid = (start + end) / 2;
            
            if(matrix[i][mid] == target) {
                return true;
            }
            else if(matrix[i][mid] < target) {
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
        }
    }
    return false;
}