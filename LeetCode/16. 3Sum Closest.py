class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(n^2) O(1)
        nums.sort()
        n = len(nums)
        r = float('inf')
        mi = float('inf')
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s, e = i + 1, n - 1
            while s < e:
                c = nums[i] + nums[s] + nums[e]
                diff = abs(c - target)
                if diff < mi:
                    mi = diff
                    r = c
                    if diff == 0:
                        return r
                if c < target:
                    s += 1
                else:
                    e -= 1
        return r