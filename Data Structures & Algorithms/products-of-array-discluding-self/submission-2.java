class Solution {
    public int[] productExceptSelf(int[] nums) {

        

        int[] list = new int[nums.length];

        for(int i=0; i<nums.length;i++){
            int j = 0;
            int pro = 1;

            while(j<nums.length){
                if(j!=i){
                    pro*=nums[j];

                }
                j++;
                
            }
            list[i]=pro;
            
        }

        return list;
        
    }
}  
