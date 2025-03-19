class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;
        int res = 0;

        // Hash all the array elements
        for (int val: nums)
            st.insert(val);

        // check each possible sequence from the start then update optimal length
        for (int val: nums) {
        
            // if current element is the starting element of a sequence
            if (st.find(val) != st.end() && st.find(val-1) == st.end()) {
            
                // Then check for next elements in the sequence
                int cur = val, cnt = 0;
                while (st.find(cur) != st.end()) {
                    
                    // Remove this number to avoid recomputation
                    st.erase(cur);
                    cur++;
                    cnt++;
                }

                // update  optimal length
                res = max(res, cnt);
            }
        }
        return res;
    }
};