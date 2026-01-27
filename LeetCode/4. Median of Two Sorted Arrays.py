class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O((m+n)log(m+n)) O(m+n)
        """
        nums1.extend(nums2)
        nums1.sort()
        nums2 = None
        leng = len(nums1)
        if leng%2==0:
            return (nums1[leng//2] + nums1[leng//2-1])/2
        else:
            return float(nums1[leng//2])"""

        # O(log(min(m, n))) O(1)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            b1 = (low + high) // 2
            b2 = (m + n + 1) // 2 - b1

            maxl1 = -inf if b1 == 0 else nums1[b1 - 1]
            minr1 = inf if b1 == m else nums1[b1]
            maxl2 = -inf if b2 == 0 else nums2[b2 - 1]
            minr2 = inf if b2 == n else nums2[b2]

            if maxl1 <= minr2 and maxl2 <= minr1:
                if (m + n) % 2 == 0:
                    return (max(maxl1, maxl2) + min(minr1, minr2)) / 2
                else:
                    return max(maxl1, maxl2)
            elif maxl1 > minr2:
                high = b1 - 1
            else:
                low = b1 + 1
        return float(max(maxl1, maxl2)) if (len(nums1) + len(nums2)) % 2 == 1 else (maxl1 + minr2) / 2
