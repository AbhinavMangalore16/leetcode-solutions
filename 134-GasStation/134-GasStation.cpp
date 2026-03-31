// Last updated: 3/31/2026, 9:39:42 PM
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int expend = 0;
        int fuel = 0;
        int ind = 0;
        for(int i =0; i< gas.size();i++){
            fuel += (gas[i]-cost[i]);
            if (fuel<0){
                expend += fuel;
                fuel = 0;
                ind = i+1;
            }
        }
        return (fuel+expend)>=0? ind:-1;
    }
};