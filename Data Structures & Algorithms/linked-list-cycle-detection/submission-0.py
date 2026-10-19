# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr_Node = head
        visit_history = set()

        while curr_Node:

            if curr_Node in visit_history:
                return True
            visit_history.add(curr_Node)
            curr_Node = curr_Node.next

        return False
        