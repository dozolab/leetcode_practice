from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        response = l3
        carry = 0
        while l1 is not None or l2 is not None:
            value = carry
            if l1 is not None:
                value = value + l1.val
                l1 = l1.next
            if l2 is not None:
                value = value + l2.val
                l2 = l2.next
            carry = value // 10
            l3.val = value % 10
            if l1 is not None or l2 is not None or carry != 0:
                l3.next = ListNode(val=carry)
                l3 = l3.next
        return response

l1=ListNode(val=2)
l1_next=ListNode(val=4)
l1.next=l1_next
l1_next_next=ListNode(val=3)
l1_next.next=l1_next_next
l2=ListNode(val=5)
l2_next=ListNode(val=6)
l2.next=l2_next
l2_next_next=ListNode(val=9)
l2_next.next=l2_next_next
l2_next_next_next=ListNode(val=9)
l2_next_next.next=l2_next_next_next
l3=Solution().addTwoNumbers(l1, l2)
while l3 is not None:
    print(l3.val)
    l3=l3.next


