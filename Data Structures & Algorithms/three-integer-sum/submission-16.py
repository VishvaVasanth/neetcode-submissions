class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        
        nums.sort()
        j = 0 
        k = 0

        res = []

        for i in range(len(nums)-2):       
            j= i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i],nums[j],nums[k]])
                    k-=1
                    while k>j and nums[k+1] == nums[k] :
                        k-=1
                    j+=1
                    while j<k and  nums[j-1]==nums[j]:
                        j+=1
                    
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                    
                else:
                    j+=1
               
        return res

