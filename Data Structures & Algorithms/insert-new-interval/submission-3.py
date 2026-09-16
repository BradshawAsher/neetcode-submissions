class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #okay so we have the newinterval and need to find which item in intervals either contains or matches the start of the newInterval
        #if there was no match/contain, then the interval in intervals with a start that is greater than newInterval's end, we will add new interval into intervals with insert.
        #we know if there is a contain/match if 
        #newInterval[0][1] <= intervals[i][1] <= newInterval[1]
        #if we find a place that we have to merge, then merge the first two, then continue forward on intervals to see if we have to continue merging



        if not intervals:
            return [newInterval]
        
        if not newInterval: 
            return intervals

        new_start = newInterval[0]
        new_end = newInterval[1]

        for i in range(len(intervals)):
            cur = intervals[i]
            start = cur[0]
            end = cur[1]

            if start > new_end:
                #then append before it
                intervals.insert(i, newInterval)
                return intervals
            
            if new_start <= end:
                #merge
                cur[1] = max(end, new_end)
                cur[0] = min(start, new_start)
                #need to continue going through the intervals to find more merging

                j = i+1
                while j < len(intervals) and cur[1] >= intervals[j][0]:
                    #merge
                    cur[1] = max(cur[1], intervals[j][1])
                    cur[0] = min(cur[0], intervals[j][0])
                    intervals.pop(j)
                
                return intervals
                    


        #if we add strictly to the back
        intervals.append(newInterval)
        return intervals



