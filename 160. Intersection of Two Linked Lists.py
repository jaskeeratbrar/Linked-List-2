# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        trackMap = {}

        while headA:
            trackMap[headA] = 1
            headA = headA.next

        while headB:
            if headB in trackMap:
                return headB
            else:
                headB = headB.next

        return None

### T(C) : O(n + m)
### S(C) : O(n + m)
        
