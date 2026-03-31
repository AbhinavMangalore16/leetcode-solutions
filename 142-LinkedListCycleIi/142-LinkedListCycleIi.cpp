// Last updated: 3/31/2026, 9:39:33 PM
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
    ListNode *detectCycle(ListNode *head) {
        if(!head||!head->next){
            return NULL;
        }
        ListNode *tortoise = head;
        ListNode *hare = head;
        do{
            tortoise = tortoise->next;
            hare = hare->next->next;
        }while((hare!=tortoise)&&(hare!=NULL)&&(hare->next!=NULL)); //Reaches common point

        if(!hare||!hare->next){
            return NULL;
        }
        else{
        hare = head;
        while(tortoise!=hare){
            hare = hare->next;
            tortoise = tortoise->next;
        }
        return tortoise;
        }
    }
};