# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2] 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        temp = head
        prev = None
        m = None
        n = None
        while temp.next != None:
            if temp.val >= x:
                n = temp
                m = prev
                break
            elif temp.val < x:
                prev = temp
                temp = temp.next
        else:
            return head
        
        if n.next == None:
            return head
        
        temp = n.next
        prev = n
        while temp != None:
            
            if temp.val < x:
                if m == None:
                    # Insert temp.val at the first position and call it m.
                    
                    if n.next == temp:
                        temp.val, prev.val = prev.val, temp.val
                        m = n
                        n = temp
                        prev = temp
                        temp = temp.next
                    else:
                        
                        newnode = ListNode(temp.val)
                        n.val, newnode.val = newnode.val, n.val
                        temp = temp.next
                        prev.next = temp
                        n.next, newnode.next = newnode, n.next
                        m = n
                        n = newnode

                else:
                    # Insert temp.val between m and n.
                    m.next, prev.next = temp, temp.next
                    temp.next = n
                    m = temp
                    temp = prev.next

            elif temp.val >= x:
                prev = temp
                temp = temp.next

        return head

       
       
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
 
# Leetcode solution
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Leetcode solution:
                    
        # Initialize a before and after list
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        # Iterate through the list to append each item to one of the above two lists
        while head:
            # If current node is less than x, we append it to before list
            if head.val < x:
                before.next = head
                before = before.next
            # If current node is greater than or equal to x, we append it to after list
            else:
                after.next = head
                after = after.next

            head = head.next

        # Last node of the after list will be the last element of the list as well
        after.next = None

        # Now we join the two lists (remember to ignore the dummy head at the beginning of each list)
        before.next = after_head.next

        return before_head.next
