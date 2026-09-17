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
        #O(logn) time -> binary search, O(m*n) space
        

        #binary search
        #timestamps are strictly increasing

        #Understand
        #Make 3 functions
        
        #Match - Hashing + Binary search?

        #Either we can use a tuple/arr as the key like ["alice, 3"]: "sad"
        #or use alice as the key and then tuple for the values
        #{alice: ("happy", 1), ("sad", 3)}
        #if we call get("alice", 2), we return the alice value that is smaller but closest to the 2

        #or can we just have a dict of dicts {"alice": {1 : "happy" , 3, "sad"}}
        #or we can have a dict of an array = {"alice": [(1, "happy"), (3, "sad")]}

        #bottleneck is how to find the closest one when do we get("alice", 2)


        if key not in self.kv:
            return ""

        #otherwise, we have to find it w/binary search
        arr = self.kv.get(key, [])
        if not arr:
            return ""

        left, right = 0, len(arr)-1
        best_option = ""
        best_time = -1

        #always look to the arr[x][0]

        while left <= right:
            mid = (left + right) // 2
            cur_time = arr[mid][0]

            if cur_time == timestamp:
                return arr[mid][1]
            
            elif cur_time < timestamp:
                if cur_time > best_time:
                    best_option = arr[mid][1]
                    best_time = cur_time
                left = mid + 1
            else:
                #cur_time > target
                right = mid - 1
        
        return best_option




