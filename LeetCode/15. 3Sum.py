class Solution:
    def threeSum(self, nums):
        nums.sort()
        r = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s, e = i + 1, n - 1
            while s < e:
                t = nums[i] + nums[s] + nums[e]
                if t < 0:
                    s += 1
                elif t > 0:
                    e -= 1
                else:
                    r.append([nums[i], nums[s], nums[e]])
                    while s < e and nums[s] == nums[s + 1]:
                        s += 1
                    while s < e and nums[e] == nums[e - 1]:
                        e -= 1
                    s += 1
                    e -= 1
        return r