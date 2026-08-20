class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        subset = []

        def back(i):
            if i>=len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            back(i+1)

            subset.pop()
            back(i+1)
        
        back(0)

        return result


        