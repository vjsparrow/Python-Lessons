# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Solution

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mid = (m + n) // 2
        merged = []
        i = 0
        j = 0
        while (i + j) < (m + n):
            if i == m:
                merged.append(nums2[j])
                j += 1
            elif j == n:
                merged.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j += 1

        if ((m + n) % 2) == 0:
            return ((merged[mid - 1] + merged[mid]) / 2)
        else:
            return (merged[mid])
        

# State the problem: We need to find the median to two sorted arrays.

# Possible inputs: [] [1], [2] [], [2] [4], [5] [4], [1, 3] [2], [5, 8, 9] [1, 2], [77] [1, 3, 4]

# What does median mean? The middle element? Or ((mid + (mid +1))/ 2)? Both. 
# If the merged list has odd numbers, then mid is the median. Otherwise, ((mid + (mid + 1)) / 2) is the median.
