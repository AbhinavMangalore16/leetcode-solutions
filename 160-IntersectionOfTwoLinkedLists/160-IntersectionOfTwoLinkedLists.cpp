// Last updated: 3/31/2026, 9:39:20 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
		ListNode *trv1 = headA, *trv2 = headB;
		while(trv1 != trv2){
			if(trv1 == NULL){
				trv1 = headB;
			}
			else{
				trv1 = trv1 -> next;
			}
			if(trv2 == NULL){
				trv2 = headA;
			}
			else{
				trv2 = trv2 -> next;
			}
		}
		return trv1;
    }
};