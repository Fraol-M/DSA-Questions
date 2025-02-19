# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        """

        prev = None

        1--- 2 --2 --1

        val = 1
        next = 

        cur.next = prev
        None --- temp
                 pre
        
        1 --2 --2 --1
        None <--1 <--2
        """



        prev = None
        cur = head

        while cur:
            new_elem = cur.val
            temp = ListNode(new_elem) # 1, None
            temp.next = prev

            cur = cur.next
            prev = temp

        while head and temp:
            if head.val != temp.val:
                return False
            head = head.next
            temp = temp.next
        return True

        
        