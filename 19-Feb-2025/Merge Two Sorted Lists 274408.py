# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next
        while list1:
            node.next = ListNode(list1.val)
            node = node.next
            list1 = list1.next
        while list2:
            node.next = ListNode(list2.val)
            node = node.next
            list2 = list2.next

        return dummy.next


            
        



        # while curr1 and curr2:
        #     curr.next = list1.
        #     curr = curr1
        #     curr.next = curr2
        #     curr = curr2
        #     curr1 = curr1.next
        #     curr2 = curr2.next
        
        # while curr1:
        #     curr.next = curr1
        #     curr = curr1
        #     curr1 = curr1.next
        # while curr2:
        #     curr.next = curr2
        #     curr = curr2
        #     curr2 = curr2.next
        # return dummy.next

        