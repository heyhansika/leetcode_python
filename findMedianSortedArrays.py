1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        # Always binary search on smaller array
4        if len(nums1) > len(nums2):
5            nums1, nums2 = nums2, nums1
6
7        m, n = len(nums1), len(nums2)
8        low, high = 0, m
9
10        while low <= high:
11            partitionX = (low + high) // 2
12            partitionY = (m + n + 1) // 2 - partitionX  # 🔥 FIX
13
14            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
15            minRightX = float('inf') if partitionX == m else nums1[partitionX]
16
17            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
18            minRightY = float('inf') if partitionY == n else nums2[partitionY]
19
20            if maxLeftX <= minRightY and maxLeftY <= minRightX:
21                if (m + n) % 2 == 0:
22                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
23                else:
24                    return max(maxLeftX, maxLeftY)
25
26            elif maxLeftX > minRightY:
27                high = partitionX - 1
28            else:
29                low = partitionX + 1
