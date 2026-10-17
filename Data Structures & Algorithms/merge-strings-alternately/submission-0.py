class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        x = 0
        y = 0

        s = ''

        while x < len(word1) and y < len(word2):

            s+=word1[x]
            s+=word2[y]
            x+=1
            y+=1

        if len(word1) == len(word2):
            return s
        elif len(word1) > len(word2):
            return s + word1[x:]
        else:
            return s + word2[y:]
                 



        

        