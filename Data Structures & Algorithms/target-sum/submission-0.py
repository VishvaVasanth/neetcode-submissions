class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def back(i,t):
            if len(nums) ==i:
                return 1 if t == target else 0

            if (i,t) in dp:
                return dp[(i,t)]
            
            dp[(i,t)] = (back(i+1,t+nums[i]) + back(i+1,t-nums[i]))

            return dp[(i,t)]
        return back(0,0)
        
        