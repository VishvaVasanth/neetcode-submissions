class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = self.robber(nums[:len(nums)-1])
        right = self.robber(nums[1:])

        return max(left,right)
        

        
        
        
    def robber(self,nums):
        rob1 ,rob2 = 0,0

        for n in nums:
            temp = max(rob2,rob1+n)
            rob1 = rob2
            rob2= temp
        return rob2
        