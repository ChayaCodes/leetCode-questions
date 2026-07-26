class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Approach #1: Brute Force
        # Try all combinations of 3 numbers.
        # Time Complexity: O(n^3) | Space Complexity: O(1)
        """
        res = float('-inf')
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, nums[i] * nums[j] * nums[k])
        return res
        """

        # Approach #2: Sorting
        # The result must be max(3 largest, 2 smallest * 1 largest).
        # Time Complexity: O(n log n) | Space Complexity: O(1) or O(n) depending on sort
        """
        nums.sort()
        option_1 = nums[-1] * nums[-2] * nums[-3]
        option_2 = nums[0] * nums[1] * nums[-1]
        return max(option_1, option_2)
        """

        # Approach #3: Single Pass / Linear Scan (Optimal)
        # Track 3 max values and 2 min values manually.
        # Time Complexity: O(n) | Space Complexity: O(1)
        max_1 = max_2 = max_3 = float("-inf")
        min_1 = min_2 = float("inf")

        for num in nums:
            # Update 3 max values
            if num > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_3 = max_2
                max_2 = num
            elif num > max_3:
                max_3 = num

            # Update 2 min values
            if num < min_1:
                min_2 = min_1
                min_1 = num
            elif num < min_2:
                min_2 = num

        option_1 = max_1 * max_2 * max_3
        option_2 = max_1 * min_1 * min_2
        return max(option_1, option_2)

        # Approach #4: Built-in Heap / Short & Clean O(n)
        # Time Complexity: O(n) | Space Complexity: O(1)
        """
        import heapq
        max_1, max_2, max_3 = heapq.nlargest(3, nums)
        min_1, min_2 = heapq.nsmallest(2, nums)
        return max(max_1 * max_2 * max_3, min_1 * min_2 * max_1)
        """