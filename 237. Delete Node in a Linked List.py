# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### 1 --> 2 --> 3 --->4
### 1 ---> 3 ---> 3 --> 4
### 1 ---> 3 ---> 4

### dummy --> 3, dummy.val --> 3, dummy.next.next --> 4

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        dummy = ListNode(node.next.val,node.next.next)

        node.next.next = None
        node.next.val = None

        node.val = dummy.val
        node.next = dummy.next

        ### T(C) : O(1)
        ### S(C) : O(1)

        

        


        
