# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        point1 = list1
        point2 = list2

        dummy = ListNode()
        tail = dummy
        while point1 and point2:
            if point2.val >= point1.val:
                tail.next = point1
                point1 = point1.next
            else:
                tail.next = point2
                point2 = point2.next
            tail = tail.next
        tail.next = point1 if point1 else point2
        return dummy.next