# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # evaluation
        # - time complexity: O(n)
        # - space complexity: O(1)

        # have 2 pointers
        # 1) one pointer for keeping tracks of the updated list
        # 2) another pointer in the further front. finding the next non-duplicated node

        # initialiation
        # create the 2 pointers of 
        if head:
            updateNode = head
            currNode = head
            currNode = currNode.next

        # iterate through the linked list
            while currNode:
                if currNode.val != updateNode.val:
                    updateNode.next = currNode
                    updateNode = updateNode.next
                currNode = currNode.next

            updateNode.next = None
        return head
    
# note:
# - try to think prove that your algorithm can solve the special case problem in the whole search space from beginning, middle and end