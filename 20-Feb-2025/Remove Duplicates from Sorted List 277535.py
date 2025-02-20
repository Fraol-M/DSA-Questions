# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        dummynode = ListNode(-1)

        ptr = dummynode
        cur = head

        while cur:

            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            ptr.next = cur
            cur = cur.next
            ptr = ptr.next
        return dummynode.next
            