class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        hash ={}

        for char in s:
            if char in hash:
                hash[char]+=1
            else:
                hash[char]=1

        
        for char in t:
            if char in hash:
                hash[char]-=1
            else:
                return False
        
        for key,value in  hash.items():

            if(value!=0):
                return False
        
        return True

         

        