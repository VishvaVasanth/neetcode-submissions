class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pre =[1]*n

        prd =1

        for i in range(n):

            pre[i]=prd

            prd*=nums[i]
        
        sf = [1]* n

        prd = 1

        for i in range( n-1, -1,-1):
            sf[i] = prd

            prd*=nums[i]

        
        for i in range(n):
            nums[i] = sf[i]*pre[i]

        return nums