# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # idea is to have 2 pointers, one is p1-> goes 2 steps at a time 
        # p2 goes 1 step at a time 
        # if any of them reach to None then we can say no cycle 
        # but without reach ing the None, if we see that the gap between p1 and p2 is 
        #decreasing or p1 and p2 become one point at any time then this is having a cycle 
        p1 , p2 = head, head # making boht the pointers point to head initially 

        while p1 and p1.next:
            
            p2 = p2.next
            p1= p1.next.next
            if p1==p2:
                return True
        return False


        