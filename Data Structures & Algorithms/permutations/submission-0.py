class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur = []
        

        def back():

            if len(nums) == len(cur):
                res.append(cur.copy())
                return
            for num in nums:
                if num in cur:
                    continue
                
                cur.append(num)
                back()
                cur.pop()


        
        back()

        return res
        