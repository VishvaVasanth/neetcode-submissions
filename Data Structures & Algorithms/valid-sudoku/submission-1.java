class Solution {
    public boolean isValidSudoku(char[][] board) {

        HashSet<String> set = new HashSet<>();

        for(int r = 0; r<board.length;r++){
            for(int c = 0; c<board[0].length;c++){
                int num = board[r][c];

                if(num=='.'){
                    continue;
                }
                if( !set.add(num+"row"+r) || !set.add(num+"col"+c) || !set.add(num + "box" + (r/3)+"-"+(c/3))){
                    return false;
                }
            }
        }

        return true;

      


        
    }
}
