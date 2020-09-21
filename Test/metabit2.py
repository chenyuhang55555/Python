# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        slow=head
        fast=head.next
        while (slow!=fast):
            if fast==None or fast.next==None:
                return False
            slow=slow.next
            fast=fast.next.next
        return True

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        ptr = head
        while ptr:
            if ptr in s:
                return True
            s.add(ptr)
            ptr=ptr.next
        return False
