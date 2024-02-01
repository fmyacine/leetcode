/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode* Q; struct ListNode* P;
    int x;
    if(head == NULL) return NULL;
    Q = head;
    while(Q->next != NULL){
        P = Q->next;
        int x = ( P != NULL) ? P->val : 0;
        if( Q->val == x){
            Q->next = P-> next;
            free(P);
        }
        else{
            Q = Q->next;
        }
    }
    return head;
}