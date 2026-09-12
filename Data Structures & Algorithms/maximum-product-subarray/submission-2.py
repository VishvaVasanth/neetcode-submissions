class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        final = nums[0]
        
        mx = nums[0]
        mn = nums[0]

        for n in nums[1:]:

            old_mx = mx
            old_mn = mn 

            mx = max(n,old_mx*n,old_mn*n)
            mn = min(n,old_mx*n,old_mn * n)
            final = max(mx,final)

        return final
       
        


        
        