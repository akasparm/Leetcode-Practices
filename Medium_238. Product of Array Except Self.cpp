class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> result_nums(nums.size(), 1);
        std::vector<int> left_mul(nums.size(), 1);
        std::vector<int> right_mul(nums.size(), 1);

        for(int i=nums.size()-2; i>=0; i--){
            right_mul[i] = right_mul[i+1]*nums[i+1];
        }
        
        for(int i=1; i<nums.size(); i++){
            left_mul[i] = left_mul[i-1]*nums[i-1];
            result_nums[i] = left_mul[i]*right_mul[i];
        }

        result_nums[0] = left_mul[0]*right_mul[0];

        return result_nums;

    }
};