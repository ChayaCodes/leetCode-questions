class Solution {
    public long countBadPairs(int[] nums) {
        long badPairs = 0;
        int n = nums.length;
        
        // Calculate total pairs (i, j) where i < j
        long totalPairs = (long) n * (n - 1) / 2;
        
        // Map to store the count of (nums[j] - j)
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int j = 0; j < n; j++) {
            int diff = nums[j] - j;
            if (map.containsKey(diff)) {
                badPairs += (j - map.get(diff));
            } else {
                badPairs += j;
            }
            map.put(diff, map.getOrDefault(diff, 0) + 1);
        }
        
        // Return the total number of bad pairs
        return badPairs;
    }
}