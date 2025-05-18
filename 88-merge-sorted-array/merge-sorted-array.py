class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        w_idx = m + n - 1
        
        while i >= 0 or j >= 0:
            if i >= 0 and (j < 0 or nums1[i] > nums2[j]):
                nums1[w_idx] = nums1[i]
                i -= 1
            else:
                nums1[w_idx] = nums2[j]
                j -= 1
            w_idx -= 1
