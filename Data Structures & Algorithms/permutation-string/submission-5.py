class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target = sorted(s1)

        n=len(s1)       

       

        for k in range(len(s2)-n+1):
            
            p = s2[k:k+n]
            

            if target==sorted(p):
                return True
        return False

        


        
        
        