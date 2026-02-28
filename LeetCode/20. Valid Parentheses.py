class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) O(n)
        if len(s)%2 == 1 or len(s) == 0:
            return False
        stack = [] # for ease of use LALO (FIFO but reversed order stack so i dont have to reorder the stack every single time)
        par = {"}":"{","]":"[",")":"("}
        for i,p in enumerate(s):
            if p in par.values():
                stack.append(p)
            else:
                if len(stack) == 0 or stack[-1]!=par[p]:
                    return False
                else:
                    del stack[-1]
        return len(stack) == 0