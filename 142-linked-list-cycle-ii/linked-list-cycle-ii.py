# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dup = {}
        cpt = 0
        while 1:
            if head == None:
                return None
            if head in dup:
                return head
            else:
                dup[head] = cpt
                cpt += 1
            head = head.next
        