class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        k = 0
        for i, el in enumerate(nums):
            if el == val:
                k += 1
            else:
                nums[i - k] = nums[i]
        return n - k
        