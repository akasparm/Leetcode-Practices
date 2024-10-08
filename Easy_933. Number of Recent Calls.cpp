class RecentCounter {
public:

    std::vector<int> recent_counters;

    RecentCounter() {
        
    }
    
    int ping(int t) {

        int counter = 0;
        recent_counters.push_back(t);

        for(const auto& count : recent_counters){
            if(count>= t-3000){
                counter++;
            }
        }

        return counter;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */