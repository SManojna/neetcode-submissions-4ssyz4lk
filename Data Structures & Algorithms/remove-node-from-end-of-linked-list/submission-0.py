# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first go till nth node
        # second pointer at head and moving both first and second till first goes to null 
        # remove the node where second is there 
        
        # iterating till nth node 
        dummy = ListNode(0, head)
        first = dummy
        for count in range (0, n+1):
            first = first.next
        second = dummy
        while first!=None:
            first = first.next
            second = second.next

        temp = second.next.next
        second.next=temp
        return dummy.next

        