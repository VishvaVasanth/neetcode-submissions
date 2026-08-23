class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res =[]

        hash = {
            2:"abc",
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }

        cur  =[]

        def back(i):
            if i==len(digits):
                res.append("".join(cur))
                return

            nums = hash[int(digits[i])] 
            
            for c in nums:
                cur.append(c)
                back(i+1)
                cur.pop()
            

        
        back(0)
        return res


        
        