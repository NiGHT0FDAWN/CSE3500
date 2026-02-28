class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # O(4^n) O(4^n*n)
        letters = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        if len(digits) == 1:
            return letters[int(digits)]
        elif len(digits) == 2:
            return [i+j for i in letters[int(digits[0])] for j in letters[int(digits[1])]]
        elif len(digits) == 3:
            return [i+j+k for i in letters[int(digits[0])] for j in letters[int(digits[1])] for k in letters[int(digits[2])]]
        else:
            return [i+j+k+l for i in letters[int(digits[0])] for j in letters[int(digits[1])] for k in letters[int(digits[2])] for l in letters[int(digits[3])]] 