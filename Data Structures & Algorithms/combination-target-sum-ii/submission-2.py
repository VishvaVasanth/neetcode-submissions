class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

       
        
        res = []
        candidates.sort()

        def back(index,cur,total):

            if target == total:
                res.append(cur.copy())
                return
            if total> target or index == len(candidates):
                return
            
            cur.append(candidates[index])
            back(index+1,cur,total+candidates[index])
            cur.pop()

            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index+=1
            back(index+1,cur,total)      
                       
        
        back(0,[],0)
        

        return res

        
        