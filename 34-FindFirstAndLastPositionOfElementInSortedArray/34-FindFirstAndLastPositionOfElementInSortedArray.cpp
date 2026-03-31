// Last updated: 3/31/2026, 9:41:01 PM
class Solution {
public:
    int binarysearch(vector<int> arr, int num, int low, int high){
        while(low<=high){
            int mid = low+(high-low)/2;
            if (arr[mid] == num){
                return mid;
            }
            else if(arr[mid] < num){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        return -1;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        int leftind, rightind;
        leftind = binarysearch(nums,target,0,nums.size()-1);
        rightind=binarysearch(nums,target,0,nums.size()-1);
        bool ans=1;
        while(ans){
            int temp = binarysearch(nums,target,0,leftind-1);
            if(temp!=-1){
                leftind = temp;
            }
            else{
                ans=0;
            }
        }
        ans=1;
        while(ans){
            int temp = binarysearch(nums,target,rightind+1,nums.size()-1);
            if(temp!=-1){
                rightind = temp;
            }
            else{
                ans=0;
            }
        }
        vector<int> answer;
        answer.push_back(leftind);
        answer.push_back(rightind);
        return answer;
        
    }
};