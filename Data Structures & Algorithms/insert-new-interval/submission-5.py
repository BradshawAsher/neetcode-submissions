class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        #Step 1: Put newInterval at the end, then slide it left until sorted by start time
        intervals.append(newInterval)
        k = len(intervals) - 1

        while k > 0 and intervals[k][0] < intervals[k - 1][0]:
            intervals[k], intervals[k - 1] = intervals[k-1], intervals[k]
            k -= 1

        #Step 2: in place two-pointer merge
        w = 0 #Write pointer tracks the end of the merged portion

        for r in range(1, len(intervals)):
            #If current read interval overlaps with the last written interval:
            if intervals[r][0] <= intervals[w][1]:
                intervals[w][1] = max(intervals[w][1], intervals[r][1])
            else:
                #No overlap: advance write pointer and overwrite
                w += 1
                intervals[w] = intervals[r]

        #Step 3: truncate remaining elements
        del intervals[w + 1: ]
        return intervals



