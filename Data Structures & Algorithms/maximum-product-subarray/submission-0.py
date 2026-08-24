class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)

        curMax = 1
        curMin = 1

        for n in nums:
            if n==0:
                curMax = 1
                curMin = 1
            temp =n*curMax
            curMax = max(n*curMax,n*curMin,n)
            curMin = min(temp,n*curMin,n)
            res=max(res,curMax)

        return res

        
        