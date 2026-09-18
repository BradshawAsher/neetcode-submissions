import bisect
class TimeMap:

    def __init__(self):
        #use a dict of arrays
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #O(1) time
        if key not in self.kv:
            self.kv[key] = []
        
        # append in place; do not re-assign the return value
        self.kv[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""

        arr = self.kv[key]

        #bisect_right with a key extracts only the timestamp for comparison
        idx = bisect.bisect_right(arr, timestamp, key=lambda x: x[0])

        #If idx == 0, all recorded timestamps are greater than the target
        return arr[idx-1][1] if idx > 0 else ""



