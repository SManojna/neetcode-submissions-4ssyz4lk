# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the len of linkedList, if len is n , then till n/2 it is one linkedlist and from n/2+1 onwards it is another linnkedList now merge both ofthem 
        # reach the mid of the linkedlist by using 2 pointers -> one whihc goes 2 stpes and one which goes 1 step
        fast, slow = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        sec = slow.next
        prev = slow.next = None
        # print(slow.val, i2.val, head.val)

        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp
        
        first , sec = head, prev
        while sec:
            temp1, temp2 = first.next, sec.next
            first.next = sec
            sec.next = temp1
            first, sec = temp1, temp2
            
        



        