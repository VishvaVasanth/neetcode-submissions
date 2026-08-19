class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lstIndex = {}

        for i,n in enumerate(s):
            lstIndex[n]=i
        size =0
        result =[]
        end = 0
        for index,num in enumerate(s):
            size+=1
            end = max(end,lstIndex[num])

            if index==end:
                result.append(size)
                size=0
        
        return result
        