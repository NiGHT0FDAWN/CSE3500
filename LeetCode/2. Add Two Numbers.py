# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # O(m+n) O(m+n)
        self.l1 = l1
        self.l2 = l2
        i, m1, m2 = 0, 0, 0
        temp = ListNode()
        while self.l1 is not None:
            i += self.l1.val * 10 ** m1
            self.l1 = self.l1.next
            m1 += 1
        while self.l2 is not None:
            i += self.l2.val * 10 ** m2
            self.l2 = self.l2.next
            m2 += 1
        current = temp
        for _ in str(i)[::-1]:
            new_node = ListNode(int(_))
            current.next = new_node
            current = current.next
        return temp.next


