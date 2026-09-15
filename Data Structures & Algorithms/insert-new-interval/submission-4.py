class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        

        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[0]:
                intervals.insert(i,newInterval)
                break
        else:
            intervals.append(newInterval)


        i=0
        while i+1 < len(intervals) and i <len(intervals):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i]=[intervals[i][0],max(intervals[i+1][1],intervals[i][1])]
                intervals.pop(i+1)
                if len(intervals)==1:
                    break
            else:
                i+=1

        return intervals

        