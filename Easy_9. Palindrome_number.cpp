class Solution {
public:
    bool isPalindrome(int x) {
        int l = 0;
        int r = std::to_string(x).size()-1;

        std::string new_x = std::to_string(x);

        while(l<r){
            std::cout << new_x[l] << " " << new_x[r] << std::endl; 
            if(new_x[l] != new_x[r]){
                std::cout << "Inside if" <<std::endl;
                return false;
            }
            l++;
            r--;
        }

        return true;
    }

    
};