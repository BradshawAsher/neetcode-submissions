import bisect
class TimeMap:

    def __init__(self):
        #use a dict of arrays
        self.times = {}
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #O(1) time
        if key not in self.times:
            self.times[key] = []
            self.vals[key] = []
        
        self.times[key].append(timestamp)
        self.vals[key].append(value)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""

        #bisect_right with a key extracts only the timestamp for comparison
        idx = bisect.bisect_right(self.times[key], timestamp)

        #If idx == 0, all recorded timestamps are greater than the target
        return self.vals[key][idx-1] if idx > 0 else ""



