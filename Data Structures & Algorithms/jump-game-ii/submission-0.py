class Solution:
    def jump(self, nums: List[int]) -> int:

        jump = 0
        curend = 0
        farend = 0

        for i in range(len(nums)-1):

            farend = max(farend,nums[i]+i)

            if curend == i:
                jump+=1
                curend =farend
        return jump

        