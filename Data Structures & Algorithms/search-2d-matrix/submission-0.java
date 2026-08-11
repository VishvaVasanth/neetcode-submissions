class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int l = 0;
        int r = matrix.length - 1;

        while (l <= r) {

            int mid = l + (r - l) / 2;

            if (matrix[mid][0] > target) {
                r = mid - 1;
            }
            else if (matrix[mid][matrix[0].length - 1] < target) {
                l = mid + 1;
            }
            else {
                return rowSearch(matrix[mid], target);
            }
        }

        return false;
    }

    private boolean rowSearch(int[] mat, int target) {

        int l = 0;
        int r = mat.length - 1;

        while (l <= r) {

            int mid = l + (r - l) / 2;

            if (mat[mid] == target) {
                return true;
            }

            if (mat[mid] > target) {
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }

        return false;
    }
}