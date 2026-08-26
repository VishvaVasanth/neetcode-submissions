class Solution:
    def hammingWeight(self, n: int) -> int:

        n = bin(n)
        one = 0

        for i in range(len(n)-1,-1,-1):

            if n[i] == '1':
                one+=1
        return one

        