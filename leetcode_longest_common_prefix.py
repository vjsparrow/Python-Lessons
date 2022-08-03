# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# Code:

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    min_len = strs[0]
    for i in strs:
        if len(i) < len(min_len):
            min_len = i

    common_pref = ""
    for i in range(len(min_len)):
        for j in range(len(strs)):
            if min_len[i] != strs[j][i]:
                return (common_pref)
        common_pref += min_len[i]
    return(common_pref)
