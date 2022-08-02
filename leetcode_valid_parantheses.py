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
            for i in range(len(s)):
                if s[i] in sopen:
                    open += s[i]
                elif s[i] in sclose:
                    if open == "":
                        return False
                    else:
                        if sopen.index(open[-1]) == sclose.index(s[i]):
                            open = open[:- 1]
                        elif sopen.index(open[-1]) != sclose.index(s[i]):
                            return False
            if open == "":
                return True
            else:
                return False
