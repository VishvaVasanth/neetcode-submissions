class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        r = len(numbers)-1

        res = []

        while i<r:
            if numbers[i]+numbers[r]>target:
                r-=1
            elif numbers[i]+numbers[r]<target:
                i+=1
            else:
                res.append(i+1)
                res.append(r+1)
                break
        return res       