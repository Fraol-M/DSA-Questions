# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        

        """
        1 2 3 4 5 6
        

        1--6
        2 --5
        3 -- 4


        n-1-i

        """

        arr = []
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length+=1

        print(length)
        middle = (length / 2) 


        cur = head

        while middle:
            arr.append(cur.val)
            middle-=1
            cur = cur.next

        i = len(arr)-1
        
        while cur:
            val = cur.val
            arr[i]+=val
            cur = cur.next
            i-=1


        return max(arr)