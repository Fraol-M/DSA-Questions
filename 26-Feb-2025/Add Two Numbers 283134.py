# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 =""
        num2 = ""

        cur1 = l1
        cur2 = l2

        while cur1:
            num1 = str(cur1.val) + num1
            cur1 = cur1.next
        
        while cur2:
            num2 = str(cur2.val) + num2
            cur2 = cur2.next
        
        num3 = str(int(num1)+ int(num2))
        dummy = curr = ListNode(-1)
        for i in range(len(num3)-1, -1, -1):
            node = ListNode(num3[i])
            curr.next = node
            curr = node
        return dummy.next 
