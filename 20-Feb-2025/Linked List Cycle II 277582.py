# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        fast = slow = head
        stat  = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                stat = True
                break
        if stat == False:
            return None
        
        start = head

        while start != fast:
            start = start.next
            fast = fast.next

        return start
