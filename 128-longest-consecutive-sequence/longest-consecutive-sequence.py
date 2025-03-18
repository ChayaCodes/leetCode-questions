class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unchecked_nums = set(nums)
        max_consecutive_length = 0
        
        for num in nums:
            if num - 1 not in unchecked_nums:
                current_length = 0
                current_num = num
                
                while current_num in unchecked_nums:
                    current_length += 1
                    unchecked_nums.remove(current_num)
                    current_num += 1

                max_consecutive_length = max(max_consecutive_length, current_length)
        
        return max_consecutive_length