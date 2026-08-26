class Solution:
    def countBits(self, n: int) -> List[int]:

        ans =[]

        for i in range(n+1):
            binary = bin(i)
            count = binary.count('1')
            ans.append(count)

        return ans 


        