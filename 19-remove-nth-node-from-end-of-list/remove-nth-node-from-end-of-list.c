/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    
    if ( head == NULL ) return head;
    
    struct ListNode* q = malloc(sizeof(struct ListNode));
    q = head; 
    int cpt = 0;

    while( q != NULL) {
        cpt++;
        q = q->next;
    }
    cpt -= n;
    q = head;
    

    if (cpt == 0) {
        struct ListNode* toRemove = head;
        head = head->next;
        free(toRemove);
    } else {
        for(int i = 0 ; i < cpt - 1 ; i++){
            q = q->next;
        }

        struct ListNode* P;
        P = q->next;
        q->next = P->next;
        free(P);
    }

    return head;
}
