class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)):
            digits[i]=str(digits[i])
        
        nums = ''.join(digits)
        nums = int(nums)
        nums+=1

        nums = str(nums)

        nums = list(nums)

        for i in range(len(nums)):
            if i>=len(digits):
                digits.append(nums[i])
                continue
            digits[i]=int(nums[i])

        return digits

    

        
        
      

        