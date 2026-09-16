class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")

        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            #1. Find the delimiter "#".
            j = i
            while s[j] != "#":
                j += 1
            
            #2. extract the length integer
            length = int(s[i:j])

            #3. Slice exactly "length" characters after "#"
            start = j + 1
            end = start + length
            res.append(s[start: end])

            #4. Advance pointer to the next encoded block
            i = end
        return res
