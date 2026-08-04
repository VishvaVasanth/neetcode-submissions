class Solution {
    public int longestConsecutive(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for(int n : nums){
            set.add(n);
        }

        int lon = 0;

        for(int num : set){

            if(!set.contains(num-1)){
                
                int cur =num;
                int len = 1;

                while(set.contains(cur+1)){
                    len++;
                    cur++;
                }

                lon = Math.max(len,lon);                   

            }
        }

        return lon;
        
    }
}
