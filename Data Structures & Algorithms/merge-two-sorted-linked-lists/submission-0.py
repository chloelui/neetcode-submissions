# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2

        ans = ListNode()
        dummy = ans

        while list1 and list2:
            curr = ListNode()
            if list1.val <= list2.val:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next
            ans.next = curr
            ans = ans.next

        while list1:
            curr = ListNode()
            curr.val = list1.val
            list1 = list1.next
            ans.next = curr
            ans = ans.next
        while list2:
            curr = ListNode()
            curr.val = list2.val
            list2 = list2.next
            ans.next = curr
            ans = ans.next

        return dummy.next