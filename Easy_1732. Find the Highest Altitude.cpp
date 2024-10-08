class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        std::vector<int> altitudes;
        altitudes.push_back(0);

        for(const auto& curr_gain : gain){
            altitudes.push_back(altitudes.back()+curr_gain);
        }

        int max_alt = 0;
        for(const auto& curr_alt : altitudes){
            if (curr_alt>max_alt){
                max_alt = curr_alt;
            }
        }

        return max_alt;
    }
};