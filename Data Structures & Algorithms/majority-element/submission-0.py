class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hash = {}
        
        n = len(nums)/2

        for num in nums:
            if num not in hash:
                hash[num]=0
            hash[num]+=1

            if hash[num] >= n:
                return num
        
            
        