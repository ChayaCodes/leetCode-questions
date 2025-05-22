class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_k = sum_k = sum(nums[:k])
        i = k

        while i < len(nums):
            sum_k = sum_k - nums[i - k] + nums[i]
            max_k = max(max_k, sum_k)
            i += 1

        return max_k / k

