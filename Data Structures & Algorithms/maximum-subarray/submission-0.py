class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur_max = nums[0]
        max_sub = nums[0]

        for i in range(1,len(nums)):
            cur_max =max(nums[i],cur_max+nums[i])
            max_sub = max(cur_max,max_sub)
        
        return max_sub
                


        