# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], addtion=0) -> Optional[ListNode]:
        val = (l1.val + l2.val + addtion) % 10
        addtion = (l1.val + l2.val + addtion) // 10

        if l1.next and l2.next:
            return ListNode(val, self.addTwoNumbers(l1.next, l2.next, addtion))
        if l1.next:
            l = l1
        elif l2.next:
            l = l2
        else:
            if addtion:
                return ListNode(val, ListNode(addtion))
            else:
                return ListNode(val)
        if addtion == 0:
            return ListNode(val, l.next)
        else:
            return ListNode(val, self.addTwoNumbers(l.next, ListNode(0), addtion))
