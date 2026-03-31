// Last updated: 3/31/2026, 9:41:04 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* fol;
        ListNode* check = curr;
        int K=1;
        while(check->next!=NULL&&K<=k)
        {
            K++;
            check=check->next;
        }
        if(K<k)
            return head;
        K=0;
        while((curr!=NULL)&&(K<k)){
            fol = curr->next;
            curr->next = prev;
            prev = curr;
            curr = fol;
            K++;
        }
        if (fol!=NULL){
            head->next = reverseKGroup(fol,k);
        }
        return prev;
    }
};