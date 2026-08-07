class Solution {
    public int maxArea(int[] heights) {

        int left =0;
        int right= heights.length-1;

        int max_cap=0;

        while(left<right){

            int len = right-left;

            if(heights[left]>heights[right]){
                if(max_cap<len*heights[right]){
                    max_cap=len*heights[right];
                }
                right--;
            }else{
                if(max_cap<len*heights[left]){
                    max_cap=len*heights[left];
                }
                left++;
            }            

        }

        return max_cap;
        
    }
}
