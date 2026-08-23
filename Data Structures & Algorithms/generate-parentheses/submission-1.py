class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def back(l,r):

            if l == r == n:
                res.append("".join(stack))
                return
            
            if l<n:
                stack.append('(')
                back(l+1,r)
                stack.pop()

            if r<l:
                stack.append(')')
                back(l,r+1)
                stack.pop()

        back(0,0)

        return res
                
            
        