class Solution:
    def checkValidString(self, s: str) -> bool:

        leftmin =0
        leftmax = 0

        for st in s:
            if st =='(':
                leftmin+=1
                leftmax+=1         
            elif st == ")":
                leftmax-=1
                leftmin-=1
            else:
                leftmax +=1
                leftmin -=1

            if leftmin<0:
                leftmin=0
            if leftmax<0:
                return False

        
        if leftmin ==0:
            return True
        else:
            return False



        

           
            

        
        