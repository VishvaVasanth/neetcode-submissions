class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash ={}
        ans=[]

        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash[i] += 1
            
            
        sorted_hash  = sorted(hash.items(), key=lambda x:x[1],reverse=True )

        for i in range(k):
            ans.append(sorted_hash[i][0])

        return ans

        

        