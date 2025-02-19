# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1)
        cur = dummyNode

        ptr_1 = list1
        ptr_2 = list2

        while ptr_1 and ptr_2:

            if ptr_1.val < ptr_2.val:
                temp = ListNode(ptr_1.val)
                cur.next = temp  
                ptr_1 = ptr_1.next
 

            else:
                temp = ListNode(ptr_2.val)
                cur.next = temp
                ptr_2 = ptr_2.next
            cur = cur.next
            
                
 
        if ptr_1:
            cur.next = ptr_1
        if ptr_2:
            cur.next = ptr_2

        return dummyNode.next

