# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = {}
        position = 0
        pointer = head

        while pointer:
            nodes[position] = pointer
            pointer = pointer.next
            position += 1

        pointer = head
        for i in range(position - 1, position - (position // 2) - 1, -1):
            swapped_node = nodes[i]
            if swapped_node != pointer.next:
                swapped_node.next = pointer.next
                pointer.next = swapped_node
            else:
                swapped_node.next = None
                pointer.next = swapped_node
                return
            pointer = pointer.next.next

        pointer.next = None