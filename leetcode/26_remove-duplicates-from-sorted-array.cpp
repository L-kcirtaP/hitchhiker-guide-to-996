class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        size_t sz = nums.size();
        if (nums.empty() || nums.size() == 1) {
            return nums.size();
        }
        int idx = 1;
        for (int j = 1; j < sz; j++) {
            if (nums[j] != nums[j - 1]) {
                nums[idx++] = nums[j];
            }
        }
        return idx;
    }
};
