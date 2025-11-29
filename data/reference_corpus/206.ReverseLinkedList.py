
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p
