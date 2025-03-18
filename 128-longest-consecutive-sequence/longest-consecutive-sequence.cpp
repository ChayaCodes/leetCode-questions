class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()) return 0;

        unordered_set<int> numSet(nums.begin(), nums.end());

        int maxCount = 0;

        for(int num : numSet){
            
            if(!numSet.count(num - 1)){
                int countNums = 1;
                int currentNum = num;

                while(numSet.count(currentNum + 1)){
                    countNums++;
                    currentNum++;
                }
                maxCount = max(maxCount, countNums);
            }
        }
        return maxCount;
    }
};