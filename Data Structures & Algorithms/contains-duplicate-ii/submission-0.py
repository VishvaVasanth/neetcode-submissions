class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hasho ={}

        for i,num in enumerate(nums):

            if num in hasho and i - hasho[num] <= k:
                return True
            hasho[num] = i
        return False
            
        