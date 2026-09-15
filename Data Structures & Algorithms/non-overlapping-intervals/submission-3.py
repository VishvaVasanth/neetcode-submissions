class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        i =0
        cnt =0
        while i+1 < len(intervals):

            if intervals[i][1]>intervals[i+1][0]:
                cnt+=1
                if intervals[i][1] > intervals[i+1][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i+1)
            else:
                i+=1
        return cnt
                
            
            
        