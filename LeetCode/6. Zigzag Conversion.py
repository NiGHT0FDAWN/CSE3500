class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # O(n) O(n)
        if numRows == 1 or len(s)<numRows:
            return s
        store = [[] for _ in range(numRows)]
        ans = ""
        for i,c in enumerate(s):
            j = i%(numRows*2-2)
            if j<numRows:
                store[j].append(c)
            else:
                store[-(j+2-numRows)].append(c)
        for i in range(numRows):
            ans += ''.join(store[i])
        return ans