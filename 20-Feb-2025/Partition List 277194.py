# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        

        less_than= ListNode(None)
        greater_than = ListNode(None)

        less_ptr = less_than
        greater_ptr = greater_than

        cur = head

        while cur:
            value = ListNode(cur.val)

            if cur.val < x:
                less_ptr.next = value
                less_ptr = less_ptr.next
            else:
                
                greater_ptr.next = value
                greater_ptr = greater_ptr.next
            cur = cur.next
         
 

        
        greater_than= greater_than.next

        less_ptr.next = greater_than

        
        return less_than.next

