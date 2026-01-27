class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Without looking for help: O(n^2) O(1)
        """for _ in range(len(nums)):
            for __ in range(len(nums[_+1:])):
                if nums[_]+nums[__+_+1] == target:
                    return([_,__+_+1])"""

        # With help: O(n) O(n)
        check = {}
        for _, n in enumerate(nums):
            a = target - n
            if a in check:
                return [check[a], _]
            check[n] = _
