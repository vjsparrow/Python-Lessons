# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
            sopen = ['(', '{', '[']
            sclose = [')', '}', ']']

            open = ""
            for item in s:
                if item in sopen:
                    open += item
                elif item in sclose:
                    if open == "":
                        return False
                    else:
                        if sopen.index(open[-1]) == sclose.index(item):
                            open = open[:- 1]
                        elif sopen.index(open[-1]) != sclose.index(item):
                            return False
            if open == "":
                return True
            else:
                return False
