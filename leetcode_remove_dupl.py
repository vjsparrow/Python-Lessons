# 83. Remove Duplicates from Sorted List
# Easy

# 5506

# 201

# Add to List

# Share
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.



# ************Solution************

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
# State the problem: Remove duplicate elements from a sorted list.
# Possible Inputs: [], [1], [1, 2, 3], [1, 1, 2, 3], [1, 2, 3, 4, 4], [1, 2, 2, 3], [1, 1, 2, 2]
# Possible strategies:
# Run through the list. Compare each element to it's next element. If the two are equal, make the current element point to the element after the next element.
# If the elements are not equal, move to the next element in the list.
# Catch the edge cases:
# Empty list: return the head if the list is empty.
# List with one element: return the head if the list has one element only.
# List with no duplicates: return the list as is if the comparison condition doesn't meet.
# List with two elements: both duplicates: will be caught by the comparison condition.
# First two elements are duplicates: will be caught by comparison condition.
# Last two elements are duplicates: will be caught by comparison condition.
# List with multiple duplicates: will be caught by the comparison consdition if the condition runs through to the end of the list.
# Implementation:

        if head == None or head.next == None:
            return head
        temp = head
        while temp.next.next != None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:                
                temp = temp.next
        # The while loop will miss the last element. Catch it.
        if temp.val == temp.next.val:
                temp.next = temp.next.next
                
        return head
        
