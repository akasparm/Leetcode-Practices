class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int peak = nums[0];

        int l = 0;

        while(l<nums.size()-1){
            if(nums[l]>nums[l+1]){
                return l;
            }
            l++;
        }

        return nums.size()-1;

    }
};