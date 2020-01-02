class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        size_t sz = nums.size();
        int idx = 0;
        for (int j = 0; j < sz; j++) {
            if (nums[j] != val) {
                nums[idx++] = nums[j];
            }
        }
        return idx;
    }
};
