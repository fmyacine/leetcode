# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cpt = 0
        arr = []
        h = head

        while h:
            cpt += 1
            arr.append(h.val)
            h = h.next
        
        h = head
        i = 0

        while h and h.next and i < cpt:
            h.val = arr[i]
            i += 1
            h = h.next
            h.val= arr[cpt - 1]
            cpt -= 1
            h = h.next
            
        if len(arr) % 2 != 0:
            h.val = arr[i]