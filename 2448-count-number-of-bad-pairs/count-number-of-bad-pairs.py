class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        bad_pairs = 0
        
        # Dictionary to store the frequency of nums[j] - j
        freq = {}
        
        for j in range(n):
            diff = nums[j] - j
            
            # Calculate the number of good pairs
            if diff in freq:
                bad_pairs += j - freq[diff]
                freq[diff] += 1
            else:
                bad_pairs += j
                freq[diff] = 1
        
        return bad_pairs
