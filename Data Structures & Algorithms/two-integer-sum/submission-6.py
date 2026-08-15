class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash ={}

        for i in range(len(nums)):

            value = target - nums[i]

            if value in hash:
                return [hash[value],i]

            else:
                hash[nums[i]] = i

        
        return [-1,-1]
        