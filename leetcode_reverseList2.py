# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
 

# Follow up: Could you do it in one pass?

# ++++++++++++++++++++++++++++++++++++++++++++++++++ #

# My solution:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

# State the problem: We need to reverse a section of a given linked list. The section will be given in the form of two integers denoting the offset of nodes from the head.

# Possible inputs: [4] -- left = 1 right = 1, [3, 4] -- left = 1 right = 2, [3, 4] -- left = 1 right = 1, [4, 3, 6, 7] -- left = 1 right = 4, [4, 3, 6, 7] -- left = 2 right = 2, [4, 3, 6, 7] -- left = 4 right = 4

# Edge cases:
    # List has one element: return the head.
    # left == right: return the head.
# Strategy:
    # We sort the list in place.
        # 1. We initialize a variable each to store the current, prev, and next nodes.
        # 2. We initialize a counter and traverse the list.
        # 3. When the counter is equal to left, we store the previous node in a variable as this node will need to point to the first element of the sorted list.
        # 4. We begin reversing the list in place. 
        # 5. We store the next node in next1 and set the current node to point to prev.
        # 4. Then we move prev to temp.
        # 5. We move temp forward to next1.
        # 6. We traverse the list and keep the counter running.
        # 7. We repeat steps 3 to 5 until counter is less than or equal to right.
        # 8. When the counter is equal to right, we make the (left - 1)th node point to the first element of the sorted list and we make the last element of the sorted list point to the (right + 1)th element.
    

        # Algorithm
        # Catch the edge cases
        if left == right or head.next is None:
            return head
        # We initialize a variable each to store the current, prev, and next nodes.
        temp = head
        next1 = prev = None
        
        # We initialize a counter and traverse the list.
        counter = 1
        while temp:
            # When the counter is equal to left, we store the next node in next1 and set the current node to point to prev.          
            if counter == left:
                # This is where the list breaks off and the section that needs to be reversed begins at temp.
                # We store the prev node in a variable as we need to make the reversed list point to it.
                begin = prev
                # We store the next node in next1 and set the current node to point to prev.
                next1 = temp.next
                temp.next = prev
                # Then we move prev to temp. This is the first node of the sorted list.
                prev = temp
                # We store the first node of the sorted list in a variable as this node will need to point to the (right+1)th node after the list is reversed.
                start = prev
                counter += 1
                # We traverse the list and keep the counter running.
                while counter <= right:
                    # We keep reversing the list until counter is less than or equal to right.
                    temp = next1
                    next1 = temp.next
                    temp.next = prev
                    prev = temp
                    counter += 1
                # Once the counter is equal to right, the last node of the section to be reversed is stored in prev and is now the first element of the reversed list.
                # We make the (left-1)th node point to prev. Remember we stored the last unsorted node in the variable 'begin'.
                # If we began sorting the list from it's first element, prev will now be the new head.
                if begin is None:
                    head = prev
                # Otherwise, the (left - 1)th node will need to point to the first node of the reversed list.
                else:
                    begin.next = prev
                # The node stored in variable 'start', the (left)th node, is now the last node of the reversed list and needs to point to the (right + 1)th node.
                start.next = next1
            # If the counter is not equal to left, we move to the next node.
            else:
                prev = temp
                temp = temp.next
                counter += 1
        return head
