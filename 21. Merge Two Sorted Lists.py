# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2): # not working
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         # do some preliminary work like setting the head of the returning list
#         out = ListNode()
#         currNodeOut = out

#         currNode1 = list1
#         currNode2 = list2

#         # iterate through both list and add it to the returning list
#         while (currNode1 and currNode2):
#             # currNodeOut.val = 69
#             if (currNode1.val <= currNode2.val):
#                 currNodeOut = currNode1
#                 # currNode1.val = 61
#                 currNode1 = currNode1.next
#             else:
#                 currNodeOut = currNode2
#                 # currNode2.val = 62
#                 currNode2 = currNode2.next
#             currNodeOut = currNodeOut.next
        
#         if currNode1:
#             currNodeOut = currNode1
#         if currNode2:
#             currNodeOut = currNode2

# note:
# - pointers in python is so messy
# - i think if you wnt to change related stuff you need to use pointers 

        
# with a starting dummy node version
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to start the merged list
        out = ListNode()
        currNodeOut = out

        currNode1 = list1
        currNode2 = list2

        # Iterate through both lists and merge
        while currNode1 and currNode2:
            if currNode1.val <= currNode2.val:
                currNodeOut.next = currNode1
                currNode1 = currNode1.next
            else:
                currNodeOut.next = currNode2
                currNode2 = currNode2.next
            currNodeOut = currNodeOut.next

        # Attach the remaining part of either list
        if currNode1:
            currNodeOut.next = currNode1
        if currNode2:
            currNodeOut.next = currNode2

        # Return the merged list (skipping the dummy node)
        return out.next
