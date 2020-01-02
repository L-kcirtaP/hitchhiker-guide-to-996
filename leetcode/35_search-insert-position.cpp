class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int lo, hi;
        lo = 0; hi = nums.size() - 1;
        if (hi == -1) { return 0; } 
        bool smaller = false;
        int pos = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            pos = mid;
            if (nums[mid] == target) { return mid; }
            else if (nums[mid] < target) {
                lo = mid + 1;
                smaller = false;
            }
            else { 
                hi = mid - 1;
                smaller = true;
            }
        }
        return smaller ?pos :pos+1;     
    }
};
